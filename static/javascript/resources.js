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

function blankResource(){
    // document.getElementById("title-resource").style.display = 'none';

    document.getElementById("resourceName").innerHTML = 'Novo recurso';
    document.getElementById("button-salvar").style.display = 'none';

    document.getElementById("resource-schedule-box").style.display = 'none';
    document.getElementById("resource-history-box").style.display = 'none';
    document.getElementById("resource-info-container-buttons").style.display = 'none';

    document.getElementById("card-info-center").style = 'display: flex;justify-content: center; width: auto;'; 
    document.getElementById("resource-container").style = 'width:50vh';     
    document.getElementById("text-container").style = 'padding:0';   
    

    document.getElementById("button-cadastrar-recurso").style = 'display: flex; justify-content:center';
       
    
    


    
}


function getResource(id) {

    // var id = parseInt(location.search.substr(1).split("&")[0].split("=")[1]);
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
        blankResource();
        // editOnResourceData();

    }



}


