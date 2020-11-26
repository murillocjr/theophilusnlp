let dvvisualizer = {
    version: "0.0.1",

    create: function (_svg, _config, _d3graph) {
        var visualizer = {};
        Object.assign(visualizer, {
            config: _config,
            svg: _svg,
            d3graph: _d3graph,
            simulation: null,
            color: null,

            _link: null,          // d3 selection of all links
            _node: null,          // d3 selection of all nodes (non-struct)
            _textNode: null,      // d3 selection of all text nodes
            _structNode: null,    // d3 selection of all struct nodes
            objectNodes: null,    // d3 selection for struct and other nodes
            allNodes: null,       // d3 selection for all Possible nodes

            updateMarkers: function (size) {
                function viewBox(x, y, w, h) { return [x + "", y + "", w + "", h + ""].join(" ") }
                function moveTo(x, y) { return "M" + x + "," + y }
                function lineTo(x, y) { return "L" + x + "," + y }

                function arrow(size) {
                    return [
                        moveTo(0, -size),
                        lineTo(size * 2, 0),
                        lineTo(0, size),
                    ].join("")
                }

                svg.selectAll("marker")
                    .transition()
                    .attr("viewBox", viewBox(0, -size, size * 2, size * 2))
                    .attr("refX", size * 2)
                    .attr("refY", 0)
                    .attr("markerWidth", size * 2)
                    .attr("markerHeight", size * 2);

                svg.selectAll("marker path")
                    .transition()
                    .attr("d", arrow(size));
            },

            _setupMarkers: function (size) {

                svg.append("defs").selectAll("marker")
                    .data(["default", "dependency", "dependants"])
                    .enter().append("marker")
                    .attr("id", (d) => d)
                    .attr("orient", "auto")
                    .attr("class", "marker")
                    .attr("size", d => d.size)
                    .attr("title", d => d.title)
                    .append("path");

                this.updateMarkers(size);
            },

            _setupLinks: function () {
                svg.append("g").selectAll("path")
                    .data(this.d3graph.links)
                    .enter().append("path")
                    .attr("class", "link")
                    .attr("marker-end", "url(#default)")
                    .style("stroke-width", (d) => d);

                this._link = svg.selectAll("path.link");
                // console.log(this.d3graph.links);
            },

            _d3graphAllNodes: function () { return this.d3graph.nodes },
            _d3graphNodes: function (type) { return this.d3graph.nodes.filter(node => node.type === type) },
            _d3graphNodesSkipped: function (type) { return this.d3graph.nodes.filter(node => node.type !== type) },

            _setupNodes: function () {

                svg.append("g").selectAll(".node")
                    .data(this._d3graphNodesSkipped("struct"))
                    .enter()
                    .append("circle")
                    .attr("class", "node")
                    .attr("r", this._radius)
                    .style("stroke-dasharray", d => d.type === "protocol" ? [5, 5] : "")  // TODO: Move to styling
                    .style("stroke-width", d => d.type === "protocol" ? 5 : 1);           // TODO: Move to styling

                svg.append("g").selectAll(".structNode")
                    .data(this._d3graphNodes("struct"))
                    .enter()
                    .append("polygon")
                    .attr("class", "structNode")
                    .attr("points", this._structurePoints)
                    .style("stroke-width", 1);


                this.objectNodes = svg.selectAll('.node, .structNode');
                // Setting up source/ dest and coloring

                this.objectNodes
                    .style("fill", d => this.color(d.group))
                    .attr("source", d => d.source)
                    .attr("dest", d => d.dest)
                    .attr("distance", d => d.distance);

                this._node = svg.selectAll('.node');
                this._structNode = svg.selectAll('.structNode');

            }.bind(visualizer),

            _radius: function (node) {
                radius = node.size
                return radius + radius * node.source / 10;
            },

            _setupSimulation: function () {

                this.simulation = d3.forceSimulation(d3.values(d3graph.nodes))
                    .force("x", d3.forceX())
                    .force("y", d3.forceY())
                    .force("center", d3.forceCenter(x / 2, y / 2)) // TODO Move to somewhere else?
                    .force("charge", d3.forceManyBody().strength(this._chargeStrength))
                    .force("link", d3.forceLink(d3graph.links)
                        .distance(this._linkDistance)
                        .strength(this._linkStrength)
                    )
                    .on("tick", this._ticked);

            },

            _linkDistance: function (link) {
                // if (link.source.filtered || link.target.filtered) {
                    // return 500;
                // }
                // return this._radius(link.source) + this._radius(link.target) + this.config.default_link_distance;
                return this._radius(link.source) + this._radius(link.target) + link.distance;
            }.bind(visualizer),

            _linkStrength: function (link) {
                if (link.source.filtered || link.target.filtered) {
                    return 0.01;
                }
                return config.default_link_strength;
            },

            _chargeStrength: function (node) {
                if (node.filtered) {
                    return -0.01;
                }
                return -node.weight * config.charge_multiplier;
            },

            _structurePoints: function (d) {
                let r = this._radius(d);
                let pts = [
                    {x: -r, y: 0},
                    {x: -r * 0.707, y: -r * 0.707},
                    {x: 0, y: -r},
                    {x: r * 0.707, y: -r * 0.707},
                    {x: r, y: 0},
                    {x: r * 0.707, y: r * 0.707},
                    {x: 0, y: r},
                    {x: -r * 0.707, y: r * 0.707},
                ];

                return pts.map(p => p.x + "," + p.y).join(" ")
            }.bind(visualizer),

            updateRadiuses: function (value) {

                this._node.transition().attr("r", this._radius);
                this._structNode.transition().attr("points", this._structurePoints);

                this.updateMarkers(value / 3);
                this.simulation.alphaTarget(0.3).restart()
            },

            reapply_charge_and_links: function () {
                this.reapply_charge();
                this.reapply_links_strength()
            },

            reapply_charge: function (value) {
                config.charge_multiplier = setDefaultValue(value, config.charge_multiplier);
                this.simulation.force("charge", d3.forceManyBody().strength(this._chargeStrength));
                this.simulation.alphaTarget(0.3).restart()
            },

            updateTextVisibility: function (visible) {
                this.config.show_texts_near_circles = visible;
                this._textNode.attr("visibility", visible ? "visible" : "hidden");
                this.simulation.alphaTarget(0.3).restart()
            },

            reapply_links_strength: function (linkStrength) {
                config.default_link_strength = setDefaultValue(linkStrength, config.default_link_strength);
                this.simulation.force("link", d3.forceLink(d3graph.links)
                    .distance(this._linkDistance)
                    .strength(this._linkStrength)
                );
                this.simulation.alphaTarget(0.3).restart()
            },

            updateCenter: function (x, y) {
                this.simulation.force("center", d3.forceCenter(x / 2, y / 2))
            },

            _setupDragging: function () {
                let dragstarted = function (d) {
                    if (!d3.event.active) this.simulation.alphaTarget(0.3).restart();
                    d.fx = d.x;
                    d.fy = d.y;
                }.bind(visualizer);

                let dragged = function (d) {
                    d.fx = d3.event.x;
                    d.fy = d3.event.y;
                }.bind(visualizer);

                let dragended = function (d) {
                    if (!d3.event.active) this.simulation.alphaTarget(0);
                    if (!d.fixed) {
                        d.fx = null;
                        d.fy = null;
                    }
                }.bind(visualizer);

                this.objectNodes
                    .call(d3.drag()
                        .on("start", dragstarted)
                        .on("drag", dragged)
                        .on("end", dragended));
            },

            _setupTexts: function () {
                svg.append("g").selectAll("text")
                    .data(this.simulation.nodes())
                    .enter()
                    .append('svg:text')
                    .attr('x', 0)
                    .attr('y', 30)
                    .attr('class', 'id')
                    .append('svg:tspan')
                    .attr('x', 0)
                    .attr('dy', 5)
                    .text(d => d.title.substring(0,20))
                    .append('svg:tspan')
                    .attr('x', 0)
                    .attr('dy', 20)
                    .text(d => d.title.substring(20,40))
                    .append('svg:tspan')
                    .attr('x', 0)
                    .attr('dy', 20)
                    .text(d => d.title.substring(40,60))


                    // .text(d => d.title.substring(0,15)+"ring. \n  \r This ");

                this._textNode = svg.selectAll("text");


            },

            _link_line: function (d) {
                const dx = d.target.x - d.source.x,
                    dy = d.target.y - d.source.y,
                    dr = Math.sqrt(dx * dx + dy * dy);

                if (dr === 0) { return "M0,0L0,0" }

                const rsource = this._radius(d.sourceNode) / dr;
                const rdest = this._radius(d.targetNode) / dr;
                const startX = d.source.x + dx * rsource;
                const startY = d.source.y + dy * rsource;

                const endX = d.target.x - dx * rdest;
                const endY = d.target.y - dy * rdest;
                return "M" + startX + "," + startY + "L" + endX + "," + endY;
            }.bind(visualizer),

            setupZoom: function (container) {
                const w = window,
                    d = document,
                    e = d.documentElement,
                    g = d.getElementsByTagName('body')[0],
                    x = w.innerWidth || e.clientWidth || g.clientWidth,
                    y = w.innerHeight || e.clientHeight || g.clientHeight;

                const zoom = d3.zoom()
                    .on("zoom", function () { svg.attr("transform", d3.event.transform) });

                container.append("rect")
                    .attr("width", x)
                    .attr("height", y)
                    .style("fill", "none")
                    .style("pointer-events", "all")
                    .lower()
                    .call(zoom);
            },

            _transform: function (d) {
                return "translate(" + d.x + "," + d.y + ")";
            },


            _ticked: function () {
                this._link.attr("d", this._link_line);
                this._node.attr("transform", this._transform);
                this._structNode.attr("transform", this._transform);
                if (config.show_texts_near_circles) {
                    this._textNode.attr("transform", this._transform);
                }
            }.bind(visualizer),

            _setupColors: function () {
                // https://github.com/mbostock/d3/wiki/Ordinal-Scales#categorical-colors
                this.color = d3.scaleOrdinal(d3.schemeCategory10);
            },

            _setupAllNodes: function () {
                this.allNodes = svg.select(".node, .structNode, text")
            },
            initialize: function () {
                this._setupColors();
                this._setupMarkers(this.config.default_circle_radius / 3);
                this._setupLinks();
                this._setupNodes();
                this._setupSimulation();
                this._setupTexts();
                this._setupDragging();
                this._setupAllNodes();
            }
        });
        return visualizer

    }
};


function setDefaultValue(value, defaultValue) {
    return (value === undefined) ? defaultValue : value;
}
