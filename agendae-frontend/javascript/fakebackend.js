// this is just a buch of functions that simulates the real backend for the mockup
/*global fakeresources*/
/*global filteredfakeresources*/
/*global Fts_fuzzy_match_async*/
/*global fuzzy_match*/
/*global currentcatalogpageindex:true*/
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
var categories,
    departments,
    statuses;

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
        res,
        elements;
    currentcatalogpageindex = 1;
    data.filteredresources = [];
    data.filters.categories = [];
    data.filters.departments = [];
    data.filters.statuses = [];
    // get checked filters

    for (it = 1; it < categories.length; it += 1) {
        if (document.getElementById('cat-el-' + it).checked) {
            data.filters.categories.push(categories[it]);
        }
    }

    for (it = 1; it < departments.length; it += 1) {
        if (document.getElementById('dep-el-' + it).checked) {
            data.filters.departments.push(departments[it]);
        }
    }


    // for (it = 1; it <= data.filtertables[2].length; it += 1) {
    //
    // }

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

function changeCatalogPage(id) {
    "use strict";
    currentcatalogpageindex = id;
    fillTableResources();
    normalizeNextPrevious(id);

}

function normalizeNextPrevious(id) {
    var previous = document.getElementById('previous-button');
    var next = document.getElementById('next-button');
    previous.onclick = function () {
        changeCatalogPage(id - 1)
    };
    next.onclick = function () {
        changeCatalogPage(id + 1)
    };

    if (currentcatalogpageindex === 1) {
        previous.onclick = '';
    }

    if (currentcatalogpageindex === pagesnumber) {
        next.onclick = '';
    }
}

function applyCatalogQuery() {
    "use strict";
    var pattern,
        patternField,
        asyncMatcher;

    patternField = document.getElementById('catalog-query');
    if (!patternField) {
        return;
    }

    pattern = patternField.value;
    if (pattern.length === 0 || pattern === "") {
        data.queriedresources = data.filteredresources;
        return;
    }

    asyncMatcher = new Fts_fuzzy_match_async(fuzzy_match, pattern, data.filteredresources, function (results) {
        // Scored function requires sorting
        var i,
            j,
            count,
            results_size;
        results = results.sort(function (a, b) {
            return b[1] - a[1];
        });
        data.queriedresources = [];
        count = 0;
        results_size = results.length;
        for (i = 0; i < results_size; i += 1) {
            if (count > results_size) {
                break;
            }
            for (j = 0; j < data.filteredresources.length; j += 1) {
                if (data.filteredresources[j].name === results[i][2]) {
                    data.queriedresources.push(data.filteredresources[j]);
                    count += 1;
                }
            }
        }
        asyncMatcher = null;
    });
    asyncMatcher.start();
}

function fillCatalogFilters() {
    // "use strict";
    var resources = data.resources,
        html = "",
        it;
    categories = [data.filtertables[0]],
        departments = [data.filtertables[1]],
        statuses = [data.filtertables[2]];
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
    // prepare the apply filters buton
    for (it = 1; it < departments.length; it += 1) {

        // html += '<li><div style="width:100%"> ';
        // html += '<label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect" for="dep-el-' + it + '">';
        // html += '<input type="checkbox" id="dep-el-' + it + '" name="dep-el-' + it + '" class="mdl-checkbox__input" >';
        // html += '<span  class="mdl-checkbox__label">' + departments[it] + '</span>';
        // html += '</label></div></li>';

        html += '<li><input type="checkbox" id="dep-el-' + it + '" name="dep-el-' + it + '" class="mdl-checkbox__input"><label for="dep-el-' + it + '">';
        html += departments[it];
        html += '</label></li>';


    }
    document.getElementById('ul-dropdown-dep').innerHTML = html;

    html = '';
    for (it = 1; it < categories.length; it += 1) {

        html += '<li><input type="checkbox" id="cat-el-' + it + '" name="cat-el-' + it + '" class="mdl-checkbox__input"><label for="cat-el-' + it + '">';
        html += categories[it];
        html += '</label></li>';

    }
    document.getElementById('ul-dropdown-cat').innerHTML = html;


}

function updateCatalog(from) {
    "use strict";
    if (from === "filter") {
        applyCatalogFilters();
    }
    if (from !== "pagination") {
        applyCatalogQuery();
    }
    fillTableResources();
}

function startCatalog() {
    "use strict";
    fillCatalogFilters();
    updateCatalog();
}


function fillTableResources() {
    "use strict";
    var it,
        html = '',
        gridresources = [],
        firstresourceindex = 0,
        maxresourcesatpage = 10,
        currentpagehtml = '<button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">#PAGENUMBER#</button>',
        otherpagehtml = '<button class="mdl-button mdl-js-button mdl-button--accent" onclick="changeCatalogPage(#PAGENUMBER#)">#PAGENUMBER#</button>',
        previouspagehtml,
        nextpagehtml,
        statuscolor = '';
    // calculated needed number of pages
    pagesnumber = Math.ceil(data.queriedresources.length / maxresourcesatpage);
    firstresourceindex = (currentcatalogpageindex - 1) * maxresourcesatpage;
    gridresources = data.queriedresources.slice(firstresourceindex, firstresourceindex + maxresourcesatpage);
    // prepare pagination
    html += '<div class="agendae-catalog-pagination">';
    // html += '<span class="agendae-resource-box-title">Página: </span>';
    if (pagesnumber > 1) {
        previouspagehtml = '<button id="previous-button" class="mdl-button mdl-js-button mdl-button--accent" onclick="changeCatalogPage(1)">Anterior</button>';
        nextpagehtml = '<button id="next-button" class="mdl-button mdl-js-button mdl-button--accent" onclick="changeCatalogPage(2)">Próxima</button>';
    } else {
        previouspagehtml = '<button id="previous-button" class="mdl-button mdl-js-button mdl-button--accent" onclick="changeCatalogPage(1)">Anterior</button>';
        nextpagehtml = '<button id="next-button" class="mdl-button mdl-js-button mdl-button--accent" onclick="changeCatalogPage(1)">Próxima</button>';
    }
    html += previouspagehtml;
    for (it = 0; it < pagesnumber; it += 1) {
        if (it + 1 === currentcatalogpageindex) {
            html += currentpagehtml.replace("#PAGENUMBER#", String(it + 1)).replace("#PAGENUMBER#", String(it + 1));
        } else {
            html += otherpagehtml.replace("#PAGENUMBER#", String(it + 1)).replace("#PAGENUMBER#", String(it + 1));
        }
    }
    html += nextpagehtml;
    html += '</div>';


    // html += '<div class="agendae-catalog-new">';
    // html += '<a class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" href=resource.html?-1>Novo recurso</a>';
    // html += '</div>';

    document.getElementById('resources-pagination').innerHTML = html;
    html = "";


    html += '<table class="resourceTable">';


    if (gridresources.length === 0) {
        // prepare no resources found card
        html += '<div class="agendae-noresource-box agendae-resource-box mdl-card mdl-shadow--2dp">';
        html += '<div class="agendae-resource-box-title"><b>Nenhum recurso encontrado!</b></div><hr>';
        html += '<div class="agendae-resource-box-text"><b><i class="material-icons">youtube_searched_for</i></b></br>';
        html += 'Tente refinar sua busca para encontrar mais resultados.';
        html += '</div>';
        html += '</div>';
    } else {
        html += '<tr>';
        html += '<td>Nome</td>';
        html += '<td>Localização</td>';
        html += '<td>Código de Patrimônio</td>';
        html += '<td>Categoria</td>';
        html += '<td>Estado</td>';
        html += '</tr>';

        var count = 0;
        for (it = 0; it < maxresourcesatpage; it += 1) {
            // prepare status text style
            if (count < gridresources.length) {
                if (gridresources[it].status === "disponível") {
                    statuscolor = "green";
                } else if (gridresources[it].status === "manutenção") {
                    statuscolor = "orange";
                }
                else {
                    statuscolor = "red";
                }
                // prepare line
                //

                html += '<tr onclick=window.location.href="resource.html?id=' + gridresources[it].id + '">';
                html += '<td style="width:20%">' + gridresources[it].name + '</td>';
                html += '<td style="width:30%">' + gridresources[it].department + "</td>";
                html += '<td style="width:20%">' + gridresources[it].id + '</td>';
                html += '<td style="width:20%">' + gridresources[it].category + '</td>';
                html += '<td style="width:10%"><b style="color:' + statuscolor + ';">' + gridresources[it].status + '</b></td>';

                html += '</tr>';

                count += 1;
            } else {
                html += '<tr>';
                html += '<td></td>';
                html += '<td></td>';
                html += '<td></td>';
                html += '<td></td>';
                html += '<td></td>';

                html += '</tr>';
            }

        }
    }


    html += '</table>';

    // apply changes
    document.getElementById('resources-grid').innerHTML = html;


}

