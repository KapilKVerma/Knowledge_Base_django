console.log("Connected example.js file - Sunburt example");

var width = 550;
var height = 600;
var radius = 250;
var color = d3.scaleOrdinal(d3.schemeCategory20);
const URL = "http://127.0.0.1:8000/data/";

fetch(URL)
  .then((data) => {
    return data.json();
  })
  .then((res) => {
    nodeData = res;
    console.log("data", res);
    sunburst(res);
  });

function sunburst(nodeData) {
  var g = d3
    .select("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

  var partition = d3.partition().size([2 * Math.PI, radius]);

  var root = d3.hierarchy(nodeData).sum(function (d) {
    return d.size;
  });

  partition(root);
  var arc = d3
    .arc()
    .startAngle(function (d) {
      return d.x0;
    })
    .endAngle(function (d) {
      return d.x1;
    })
    .innerRadius(function (d) {
      return d.y0 + 20;
    })
    .outerRadius(function (d) {
      return d.y1 + 20;
    })
    .cornerRadius(0.01);

  var arc2 = d3
    .arc()
    .startAngle(function (d) {
      return d.x0 + 0.015;
    })
    .endAngle(function (d) {
      return d.x1 - 0.015;
    })
    .innerRadius(function (d) {
      return d.y0 + 24;
    })
    .outerRadius(function (d) {
      return d.y1 + 17;
    })
    .cornerRadius(2);

  g.selectAll("g")
    .data(root.descendants())
    .enter()
    .append("g")
    .attr("class", "node")
    .append("path")
    .attr("display", function (d) {
      return d.depth ? null : "none";
    })
    .attr("d", arc)
    .style("stroke", "#fff")
    .style("fill", function (d) {
      return color((d.children ? d : d.parent).data.source);
    })
    .style("cursor", "pointer")
    .on("mouseover", function (d) {
      d3.select(this).transition().duration(400).attr("d", arc2);
      d3.select("#text").text(
        "Name: " + d.data.name + " | Size:" + d.data.size
      );
    })
    .on("mouseout", function (d) {
      d3.select(this).transition().duration(400).attr("d", arc);
    })
    .on("click", function (d) {
      return alert(d.data.name + " has been clicked.");
    });

  g.selectAll(".node")
    .append("text")
    .attr("transform", function (d) {
      return (
        "translate(" +
        arc.centroid(d) +
        ")rotate(" +
        computeTextRotation(d) +
        ")"
      );
    })
    .attr("dx", "-21") // radius margin
    .attr("dy", ".5em") // rotation align
    .text(function (d) {
      return d.parent ? d.data.name : "";
    })
    .style("cursor", "pointer")
    .style("font", "12px arial")
    .style("font-weight", "400");

  function computeTextRotation(d) {
    var angle = ((d.x0 + d.x1) / Math.PI) * 90;
    return angle;
  }
}
