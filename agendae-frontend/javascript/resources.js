/**
 * Created by Caio on 11/11/2016.
 */

var editInfo = false;
var editSchedule = false;

function getResourceInfo(id) {


    var html = '';
    var it;

    //Fill fields
    //getResourceById
    var resource = data.resources[id - 1];
    var field_name = document.getElementById('text-resource-name');
    var field_loc = document.getElementById('text-resource-location');
    var field_id = document.getElementById('text-resource-id');
    var field_cat = document.getElementById('text-resource-cat');
    var field_desc = document.getElementById('text-resource-desc');

    field_name.value = resource.name;
    field_loc.value = resource.department;
    field_id.value = resource.id;
    field_cat.value = resource.category;
    field_desc.value = resource.description;
    document.getElementById('resourceName').innerHTML = resource.name;



    //History table
    html += '<table id="history-table" class="resourceTable">';
    html += '<tr>';

    html += '<td>Funcionário</td>';
    html += '<td>Agendamento</td>';
    html += '<td>Retorno</td>';
    html += '</tr>';

    for(it = 0 ; it < fakehistory.length; it += 1){
        html += '<tr>';
        html += '<td>' + fakehistory[it].username + '</td>';
        html += '<td>' + fakehistory[it].date + '</td>';
        html += '<td>' + fakehistory[it].return + '</td>';
        html += '</tr>';
    }

    html += '</table>';
    document.getElementById('table-history').innerHTML = html;

    //Fill Time Picker
    html='';
    for(it=0 ; it <schedule.length ; it+=2){

    }



    //Calendar
    new Kalendae('date-picker', {
        months: 1,
        mode: 'single',
        selected: Kalendae.moment(),
        subscribe: {
            'change': function (date) {
                //getDateSchedules
                console.log(date, this.getSelected());
                document.getElementById('date-title').innerHTML = '<b>'+this.getSelected()+'</b>';
                fillTableSchedule(this.getSelected());
            }
        }
    });


    //Availability
    //getAvailability
    if(fakeavailability.status === "ON"){
        document.getElementById('resource-availability').checked=true;
    } else {
        document.getElementById('resource-availability').checked=false;
    }


}

function fillTableSchedule(date){

}


function getResourceHistory(id) {
    var html = '';

    html += '<div class="agendae-resource-box-title"><b>Histórico</b></div>';


    // apply changes
    document.getElementById('resource-history').innerHTML = html;
}

function scheduleResource(id) {
    var html = '';

    html += '<button id="editResourceSchedule" class="hidden"  onclick=""><img src="images/ic_mode_edit_white_24dp_1x.png""></button>';
    html += '<div class="agendae-resource-box-title"><b>Agendamento</b></div>';


    // apply changes
    document.getElementById('resource-schedule').innerHTML = html;
}

function getResource() {

    var id = parseInt(location.search.substr(1).split("&")[0].split("=")[1]);
    //if normal
    // if (id > 0) {
    //         getResourceInfo(id);
    //         scheduleResource(id);
    // }


   //if admin
    if (id > 0) {
        getResourceInfo(id);
        // scheduleResource(id);
        // getResourceHistory(id);
        // adminOn();
    } else {
        // blankResource();
        // editOnResourceData();

    }



}

function adminOn() {


}






function editOnResourceData() {
    editInfo = true;
    var htmlName = '';
    var htmlDesc = '';
    var htmlDept = '';
    var htmlCat = '';
    var htmlStats = '';

    htmlName += '<input type="text" id="nameTextField" class="textfield-resource-info"  value="' + document.getElementById('resourceDataName').innerHTML + '">';
    document.getElementById('resourceDataName').innerHTML = htmlName;

    htmlDesc += '<input type="text" id="nameTextDesc" class="textfield-resource-info" value="' + document.getElementById('resourceDataDesc').innerHTML + '">';
    document.getElementById('resourceDataDesc').innerHTML = htmlDesc;

    htmlDept += '<input type="text" id="deptTextField" class="textfield-resource-info" value="' + document.getElementById('resourceDataDept').innerHTML + '">';
    document.getElementById('resourceDataDept').innerHTML = htmlDept;

    htmlCat += '<input type="text" id="catTextField" class="textfield-resource-info"  value="' + document.getElementById('resourceDataCat').innerHTML + '">';
    document.getElementById('resourceDataCat').innerHTML = htmlCat;

    htmlStats += '<input type="text" id="statsTextField" class="textfield-resource-info"  value="' + document.getElementById('resourceDataStats').innerHTML + '">';
    document.getElementById('resourceDataStats').innerHTML = htmlStats;


    document.getElementById('editResourceData').onclick = function () {
        editOffResourceData()
    };

}
function editOffResourceData() {
    editInfo = false;
    var htmlName = '';
    var htmlDesc = '';
    var htmlDept = '';
    var htmlCat = '';
    var htmlStats = '';

    htmlName += document.getElementById('nameTextField').value;
    document.getElementById('resourceDataName').innerHTML = htmlName;

    htmlDesc += document.getElementById('nameTextDesc').value;
    document.getElementById('resourceDataDesc').innerHTML = htmlDesc;

    htmlDept += document.getElementById('deptTextField').value;
    document.getElementById('resourceDataDept').innerHTML = htmlDept;

    htmlCat += document.getElementById('catTextField').value;
    document.getElementById('resourceDataCat').innerHTML = htmlCat;

    htmlStats += document.getElementById('statsTextField').value;
    document.getElementById('resourceDataStats').innerHTML = htmlStats;


    document.getElementById('editResourceData').onclick = function () {
        editOnResourceData()
    };
}
function editOnResourceSchedule() {
    editSchedule = true;

    document.getElementById('editResourceData').onclick = function () {
        editOffResourceSchedule()
    };
}
function editOffResourceSchedule() {
    editSchedule = false;

    document.getElementById('editResourceData').onclick = function () {
        editOnResourceSchedule()
    };
}

function updateInfoResource() {
    if (editInfo) {
        editOffResourceData();
    }
    var resourceToUpdate = {
        name: document.getElementById('resourceDataName').textContent,
        department: document.getElementById('resourceDataDept').textContent,
        id: document.getElementById('resourceDataId').textContent,
        status: document.getElementById('resourceDataStats').textContent,
        description: document.getElementById('resourceDataDesc').textContent,
        category: document.getElementById('resourceDataCat').textContent,
    };

    var xmlhttp = new XMLHttpRequest();



    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == XMLHttpRequest.DONE ) {
            if (xmlhttp.status == 200) {
                xmlhttp.responseText;
            }
            else if (xmlhttp.status == 400) {
                alert('There was an error 400');
            }
            else {
                alert('something else other than 200 was returned');
            }
        }
    };

    xmlhttp.open("GET", "ajax_info.txt", true);
    xmlhttp.send();
}


