//  ===================================================
//  =============== PARSING ===========================
//  ===================================================
// Input 
// { links : [ {source: sourceName, dest : destName} * ] }
// Output:
let objcdv = {
    version: "0.0.1",
    _createGraph: function (_objects) {
        return {
            nodes: [],
            links: [],
            nodesSet: {},
            objects: setDefaultValue(_objects, []),

            addLink: function (link) {

                var source_node = this.getNode(link.source);
                source_node.source++;

                var dest_node = this.getNode(link.dest);
                dest_node.dest++;

                this.links.push({
                    // d3 js properties
                    source: source_node.idx,
                    target: dest_node.idx,

                    // Additional link information
                    sourceNode: source_node,
                    targetNode: dest_node,
                    distance: link.distance
                })
            },

            getNode: function (nodeName) {
                var node = this.nodesSet[nodeName];
                if (node == null) {
                    var idx = Object.keys(this.nodesSet).length;
                    let object = setDefaultValue(this.objects[nodeName], {})
                    this.nodesSet[nodeName] = node = {idx: idx, name: nodeName, source: 1, dest: 0, type: object.type, size: object.size, title: object.title};
                }
                return node
            },

            updateNodes: function (f) {
                _.values(this.nodesSet).forEach(f)
            },

            d3jsGraph: function () {
                // Sorting up nodes, since, in some cases they aren't returned in correct number
                var nodes = _.values(this.nodesSet).slice(0).sort((a, b) => a.idx - b.idx);
                return {nodes: nodes, links: this.links};
            },

            nodesStartingFromNode: function (node, {max_level = 1000, use_backward_search = false, use_forward_search = true } = {} ) {
                // Figure out the neighboring node id's with brute strength because the graph is small
                var neighbours = {};
                neighbours[node.index] = node;

                var nodesToCheck = [node.index];
                let current_level = 0;
                while (Object.keys(nodesToCheck).length != 0) {
                    var forwardNeighbours = [];
                    var backwardNeighbours = [];

                    let tmpNeighbours = {};
                    if (use_forward_search) {
                        forwardNeighbours = this.links
                            .filter((link) => link.source.index in neighbours)
                            .filter((link) => !(link.target.index in neighbours))
                            .map((link) => {
                                tmpNeighbours[link.target.index] = link.target;
                                return link.target.index;
                            });
                    }
                    if (use_backward_search) {
                        backwardNeighbours = this.links
                            .filter((link) => link.target.index in neighbours)
                            .filter((link) => !(link.source.index in neighbours))
                            .map((link) => {
                                tmpNeighbours[link.source.index] = link.source;
                                return link.source.index;
                            });
                    }

                    _.extend(neighbours, tmpNeighbours);


                    nodesToCheck = forwardNeighbours.concat(backwardNeighbours);
                    console.log("Nodes to check" + nodesToCheck);

                    // Skip if we reached max level
                    current_level++;
                    if (current_level == max_level) {
                        console.log("Reached max at level" + current_level);
                        break;
                    }
                }
                return _.values(neighbours);

            },

            nodesStartingFromNodeByDistance: function (node, max_distance) {
                var neighbours = {};
                let tmpNeighbours = this.links
                    .filter((link) => (link.source.idx == node.idx || link.target.idx == node.idx) )
                    .map((link) => {
                        if(link.distance < max_distance){
                            neighbours[link.source.idx] = link.source;
                            neighbours[link.target.idx] = link.target;
                            // console.log(link.source.idx+','+link.distance+','+link.target.idx)
                        }
                    });
                return _.values(neighbours);
            }

        };

    },
    _createPrefixes: function () {
        return {
            _prefixesDistr: {},

            _sortedPrefixes: null,

            addName: function (name) {
                this._sortedPrefixes = null;

                var prefix = name.substring(0, 2);
                if (!(prefix in this._prefixesDistr)) {
                    this._prefixesDistr[prefix] = 1;
                } else {
                    this._prefixesDistr[prefix]++;
                }
            },

            prefixIndexForName: function (name) {
                var sortedPrefixes = this._getSortedPrefixes();
                var prefix = name.substring(0, 2);
                return _.indexOf(sortedPrefixes, prefix)
            },

            _getSortedPrefixes: function () {
                if (this._sortedPrefixes == null) {
                    this._sortedPrefixes = _.map(this._prefixesDistr, (v, k) => ({"key": k, "value": v}))
                        .sort((a, b) => b.value - a.value)
                        .map(o => o.key)
                }
                return this._sortedPrefixes
            }
        };
    },


    parse_dependencies_graph: function (dependencies) {

	//console.log(dependencies);

        var graph = this._createGraph(dependencies.objects);
        var prefixes = this._createPrefixes();

        dependencies.links
            .filter(link => link.source != link.dest)
            .forEach(link => {

                graph.addLink(link);

                prefixes.addName(link.source);
                prefixes.addName(link.dest);
            });

        // Make sure all nodes are present, even if they aren't connected
        if (dependencies.objects != null) {
            for (p in dependencies.objects) {
                graph.getNode(p)
            }
        }

        graph.updateNodes((node) => {
            node.weight = node.source;
            node.group = prefixes.prefixIndexForName(node.name) + 1
        });

        return graph

    }

};


function setDefaultValue(value, defaultValue){
    return (value === undefined) ? defaultValue : value;
}


