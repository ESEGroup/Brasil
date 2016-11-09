// this is just a buch of functions that simulates the real backend for the mockup
/*global fakeresources*/
/*global filteredfakeresources*/
/*global Fts_fuzzy_match_async*/
/*global fuzzy_match*/
/*jslint browser:true*/

var data = {
        filtertables: ["Categorias", "Departamentos", "Disponibilidade"],
        filters: {
            categories: [],
            departments: [],
            statuses: []
        },
        resources: fakeresources,
        filteredresources: filteredfakeresources,
        queriedresources: filteredfakeresources
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

function hideCatalogFilterTable(table) {
    "use strict";
    var i,
        elements = document.getElementsByClassName("table-el-" + table),
        displayState = (elements[0].style.display === "none") ? "" : "none";
    for (i = 0; i < elements.length; i += 1) {
        elements[i].style.display = displayState;
    }
    document.getElementById('table-nm-' + table).innerHTML = (displayState === "") ? '<b>' + table + '</b><i class="material-icons">expand_less</i>' : '<b>' + table + '</b><i class="material-icons">expand_more</i>';
}

function fillCatalogResources() {
    "use strict";
    var it,
        html;
    html = "";
    if (data.queriedresources.length === 0) {
      //todo: embelezr essa mensagem
        html += '<div class="mdl-card mdl-shadow--2dp">';
        html += "[WIP] NENHUM RECURSO ENCONTRADO";
        html += '</div>';
    }
    for (it = 0; it < data.queriedresources.length; it += 1) {
        if (it % 3 === 0) {
            html += '<div class="mdl-grid">';
        }
        html += '<div class="mdl-cell mdl-cell--4-col">';
        html += '<div class="mdl-card mdl-shadow--2dp" style="width:100%">';
        html += "[WIP] TESTE";
        html += '</div>';
        html += '</div>';
        if (it % 3 === 2) {
            html += "</div></br>";
        }
    }
    document.getElementById('resources-grid').innerHTML = html;
}

function applyCatalogQuery() {
    "use strict";
    var it,
        resourcename,
        pattern,
        patternField,
        asyncMatcher,
        filteredresourcesnames,
        queriedresourcesnames;

    patternField = document.getElementById('catalog-query');
    if (!patternField) {
        return;
    }

    pattern = patternField.value;
    if (pattern.length === 0 || pattern === "") {
        data.queriedresources = data.filteredresources;
        return;
    }

    filteredresourcesnames = [];
    queriedresourcesnames = [];
    for (it = 0; it < data.filteredresources.length; it += 1) {
        resourcename = data.filteredresources.name;
        filteredresourcesnames.push(resourcename);
    }

    asyncMatcher = new Fts_fuzzy_match_async(fuzzy_match, pattern, data.filteredresources, function (results) {
        // Scored function requires sorting
        var i,
            j,
            count,
            results_size,
            resources_size;
        results = results
            .sort(function (a, b) { return b[1] - a[1]; });
        data.queriedresources = [];
        count = 0;
        results_size = results.length;
        resources_size = data.filteredresources.length;
        for (i = 0; i < resources_size; i += 1) {
            if (count > results_size) {
                break;
            }
            for (j = 0; j < results_size; j += 1) {
                if (data.filteredresources[i].name === results[j]) {
                    data.queriedresources.push(data.filteredresources[i]);
                    count += 1;
                }
            }
        }
        asyncMatcher = null;
    });
    asyncMatcher.start();
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
        html += '<th class="mdl-data-table__cell--non-numeric"> <a id="table-nm-' + tables[it][0] + '" style="cursor: pointer;" onclick="hideCatalogFilterTable(\'' + tables[it][0] + '\')"><b>' + tables[it][0] + '</b><i class="material-icons">expand_more</i></a></th>';
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
    html += '<button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" onclick="updateCatalog()">';
    html += 'Aplicar Filtros';
    html += '</button>';
    document.getElementById('filter-tables').innerHTML = html;
}

function updateCatalog() {
    "use strict";
    applyCatalogFilters();
    applyCatalogQuery();
    fillCatalogResources();
}
