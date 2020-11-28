//  ===================================================
//  ===============  SELECTING_NODE       =============
//  ===================================================

let graph_actions = {
    create: function (svg, dvgraph) {

        return {
            selectedIdx: -1,
            selectedType: "normal",
            svg: svg,
            selectedObject: {},
            dvgraph: dvgraph,

            deselect_node: function (d) {
                this._unlockNode(d);
                this.selectedIdx = -1;
                this.selectedObject = {};

                this.svg.selectAll('.node, .structNode')
                    .each(function (node) {
                        node.filtered = false
                    })
                    .classed('filtered', false)
                    .transition();

                this.svg.selectAll('path, text')
                    .classed('filtered', false)
                    .transition();


                this.svg.selectAll('.link')
                    .attr("marker-end", "url(#default)")
                    .classed('filtered', false)
                    .classed('dependency', false)
                    .classed('dependants', false)
                    .transition();
            },

            deselect_selected_node: function () {
                this.deselect_node(this.selectedObject)
            },

            _lockNode: function (node) {
                node.fixed = true;
                node.fx = node.x;
                node.fy = node.y;
            },

            _unlockNode: function (node) {
                delete node.fixed;
                node.fx = null;
                node.fy = null;
            },

            _selectAndLockNode: function (node, type) {
                this._unlockNode(this.selectedObject);
                this.selectedIdx = node.idx;
                this.selectedObject = node;
                this.selectedType = type;
                this._lockNode(this.selectedObject);
            },

            _deselectNodeIfNeeded: function (node, type) {
                if (node.idx === this.selectedIdx && this.selectedType === type) {
                    this.deselect_node(node);
                    return true;
                }
                return false;
            },

            _fadeOutAllNodesAndLinks: function () {
                // Fade out all circles
                this.svg.selectAll('.node, .structNode')
                    .classed('filtered', true)
                    .each(function (node) {
                        node.filtered = true;
                        node.neighbours = false;
                    }).transition();

                this.svg.selectAll('text')
                    .classed('filtered', true)
                    .transition();

                this.svg.selectAll('.link')
                    .classed('dependency', false)
                    .classed('dependants', false)
                    .transition()
                    .attr("marker-end", "");

            },

            _highlightNodesWithIndexes: function (indexesArray) {
                this.svg.selectAll('.node, .structNode, text')
                    .filter((node) => indexesArray.indexOf(node.index) > -1)
                    .classed('filtered', false)
                    .each((node) => {
                        node.filtered = false;
                        node.neighbours = true;
                    })
                    .transition();
            },

            _isDependencyLink: (node, link) =>  (link.source.index === node.index),
            _nodeExistsInLink: (node, link) => (link.source.index === node.index || link.target.index === node.index),
            _oppositeNodeOfLink: (node, link) => (link.source.index === node.index ? link.target : link.target.index === node.index ? link.source : null),

            _highlightLinksFromRootWithNodesIndexes: function (root, nodeNeighbors) {
                this.svg.selectAll('.link')
                    .filter((link) => nodeNeighbors.indexOf(link.source.index) > -1)
                    .classed('filtered', false)
                    .classed('dependency', (l) => this._nodeExistsInLink(root,l) && this._isDependencyLink(root, l))
                    .classed('dependants', (l) => this._nodeExistsInLink(root,l) && !this._isDependencyLink(root, l))
                    // .attr("marker-end", (l) => this._nodeExistsInLink(root,l) ? (this._isDependencyLink(root, l) ? "url(#dependency)" : "url(#dependants)") : (maxLevel == 1 ? "" : "url(#default)"))
                    .transition();
            },

            selectNodesStartingFromNode: function (node, max_distance ) {

                this._selectAndLockNode(node);

                let neighborIndexes =
                    this.dvgraph.nodesStartingFromNodeByDistance(
                        node, 
                        max_distance
                    )
                    .map((n) => n.index);

                console.log(node)
                console.log(neighborIndexes)

                this._fadeOutAllNodesAndLinks();
                this._highlightNodesWithIndexes(neighborIndexes);
                // this._highlightLinksFromRootWithNodesIndexes(node, neighborIndexes);
            }

        };
    }
};

