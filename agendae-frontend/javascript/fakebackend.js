// this is just a buch of functions that simulates the real backend for the mockup
/*global fakeresources*/
/*global filteredfakeresources*/
/*jslint browser:true*/

var data = {
        filtertables: ["Categorias", "Departamentos", "Disponibilidade"],
        filters: {
            categories: [],
            departments: [],
            statuses: []
        },
        resources: fakeresources,
        filteredresources: filteredfakeresources
    };

function doLogin() {
    "use strict";
    if (document.getElementById('username').value === "admin") {
        if (document.getElementById('userpass').value === "admin") {
            window.location = "catalog.html";
            return true;
        }
    }
    document.getElementById('loginfail').style.display = "inline";
    return false;
}

function applyCatalogFilters() {
    "use strict";
    var tables = data.filtertables,
        it,
        jt,
        res,
        elements;
    data.filteredresources = [];
    // get checked filters
    for (it = 0; it < tables.length; it += 1) {
        elements = document.getElementsByClassName("table-el-" + tables[it]);
        for (jt = 0; jt < elements.length; jt += 1) {
            if (elements[jt].className.indexOf("is-selected") > -1) {
                if (it === 0) { // category
                    data.filters.categories.push(document.getElementById("table-el-" + tables[it] + "-" + String(jt)).innerText);
                }
                if (it === 1) { // departments
                    data.filters.departments.push(document.getElementById("table-el-" + tables[it] + "-" + String(jt)).innerText);
                }
                if (it === 2) { // statuses
                    data.filters.statuses.push(document.getElementById("table-el-" + tables[it] + "-" + String(jt)).innerText);
                }
            }
        }
    }
    // select final resources
    for (it = 0; it < data.resources.length; it += 1) {
      // will select the resource if a filtered field is matched or the filtered field has no selected values
        if (data.filters.categories.indexOf(data.resources[it].category) !== -1 || data.filters.categories.length === 0) {
            if (data.filters.departments.indexOf(data.resources[it].department) !== -1 || data.filters.departments.length === 0) {
                if (data.filters.statuses.indexOf(data.resources[it].status) !== -1 || data.filters.statuses.length === 0) {
                    res = data.resources[it];
                    data.filteredresources.push(res);
                }
            }
        }
    }
}

function hideCatalogTable(table) {
    "use strict";
    var i,
        elements = document.getElementsByClassName("table-el-" + table),
        displayState = (elements[0].style.display === "none") ? "" : "none";
    for (i = 0; i < elements.length; i += 1) {
        elements[i].style.display = displayState;
    }
    document.getElementById('table-nm-' + table).innerHTML = (displayState === "") ? '<b>' + table + '</b><i class="material-icons">expand_less</i>' : '<b>' + table + '</b><i class="material-icons">expand_more</i>';
}

function fillCatalogFilters() {
    "use strict";
    var resources = data.resources,
        html = "",
        categories = [data.filtertables[0]],
        departments = [data.filtertables[1]],
        statuses = [data.filtertables[2]],
        tables,
        it,
        jt;
    // get unique filter values
    for (it = 0; it < resources.length; it += 1) {
        if (categories.indexOf(resources[it].category) < 0) {
            categories.push(resources[it].category);
        }
        if (departments.indexOf(resources[it].department) < 0) {
            departments.push(resources[it].department);
        }
        if (statuses.indexOf(resources[it].status) < 0) {
            statuses.push(resources[it].status);
        }
    }
    // create tables
    tables = [categories, departments, statuses];
    for (it = 0; it < tables.length; it += 1) {
        // set table head
        html += '<table class="mdl-data-table mdl-js-data-table mdl-data-table--selectable mdl-shadow--2dp"  width="100%" id="table-' + tables[it][0] + '">';
        html += '<thead>';
        html += '<tr>';
        html += '<th class="mdl-data-table__cell--non-numeric"> <a id="table-nm-' + tables[it][0] + '" style="cursor: pointer;" onclick="hideCatalogTable(\'' + tables[it][0] + '\')"><b>' + tables[it][0] + '</b><i class="material-icons">expand_more</i></a></th>';
        html += '</tr>';
        html += '</thead>';
        html += '<tbody>';
        // set table values
        for (jt = 1; jt < tables[it].length; jt += 1) {
            html += '<tr class="table-el-' + tables[it][0] + '" style="display: none;">';
            html += '<td id="table-el-' + tables[it][0] + '-' + String(jt - 1) + '" class="mdl-data-table__cell--non-numeric">' + tables[it][jt] + '</td>';
            html += '</tr>';
        }
        // end table
        html += '</tbody>';
        html += '</table>';
        html += '<br>';
    }
    // prepare the apply filters buton
    html += '<button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" onclick="applyCatalogFilters()">';
    html += 'Aplicar Filtros';
    html += '</button>';
    document.getElementById('filter-tables').innerHTML = html;
}
