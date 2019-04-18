document.addEventListener("DOMContentLoaded", function () {
  var stage = new NGL.Stage("viewport");
  stage.loadFile("{{MEDIA_URL}}{{gpcr.mapping_pdb_file}}", {defaultRepresentation: true});
});

var __stage;
// var __nterm_color = "#78db00";
// var __cterm_color = "#c7c7c7";
// var __colors = [
//   "#7f7f7f",
//   "#1f77b4",
//   "#ff7f0e",
//   "#2ca02c",
//   "#d62728",
//   "#9467bd",
//   "#8c564b",
//   "#e377c2",
//   "#bcbd22",
//   "#17becf",
//   "#aec7e8",
//   "#ffbb78",
//   "#98df8a",
//   "#ff9896",
//   "#c5b0d5",
//   "#c49c94",
//   "#f7b6d2",
//   "#6a0893",
//   "#dbdb8d",
//   "#9edae5",
//   "#fffac8",
//   "#800000",
//   "#ffd8b1",
//   "#d2f53c",
//   "#e6beff",
//   "#e6beff",
//   "#303030"
// ]

$(document).ready(function () {
  class Legend {
    constructor(target) {
      this.ele = $(target);
      this.body = $(target + " > tbody");
    }

    clear() {
      this.body.empty();
    }

    addItem(color, name, size) {
      let row = "<tr>";
      row += "<td style='background:" + color + ";'></td>";
      row += "<td>" + name + "</td>";
      row += "<td>" + size + "</td>";
      row += "</tr>";
      this.body.append(row);
    }
  }

  // $.extend($.tablesorter.themes.bootstrap, {
  //   icons: 'fa',
  //   sortNone: 'fa-sort',
  //   sortAsc: 'fa-sort-asc',
  //   sortDesc: 'fa-sort-desc'
  // });

  // $("#mapping_counts").tablesorter({
  //   theme: 'bootstrap',
  //   widgets: ['uitheme', 'columns'],
  //   headerTemplate: '{content} {icon}',
  //   sortList: [[0,0], [1,0], [2,0], [4,0]]
  // });

  __stage = new NGL.Stage("view-stage", {
    backgroundColor: "white"
  });
  // var legend = new Legend("#view-legend");

  $('.vis-loader').each(function (i, e) {
    ele = $(e);
    model_url = ele.attr('url');

    ele.click(make_loader(model_url, legend));
  });
});
