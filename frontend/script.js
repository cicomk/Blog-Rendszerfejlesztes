fetch('http://localhost:5000/api')
.then(response => response.text())
.then(data => {});

function start(){
    list();
    categoryList();
}

function list(type_id = ''){
    
    fetch('http://localhost:5000/topics?param='+type_id)
    .then(response => response.json())
    .then(data => {
        let mes = ""
        document.getElementById('message').innerHTML = "";
        if (data.length == 0) {
            document.getElementById('message').innerHTML = "Nincs megjeleníthető tartalom";
        } else {
        for (let i = 0; i < data.length; i++) {
            // Létrehozunk egy új div elemet
            
            let div = "<div id='" + data[i].id + "'>";
            var tempVar = data[i].type_id;
            //console.log(getType(tempVar.toString()) );
            div+="<h1>" + data[i].name + "</h1><h6 id='type" + data[i].id + "'>Kategória: " + "</h6><p>" + data[i].description +"</p><hr></div>";
            document.getElementById('message').innerHTML+= div;
            getType(data[i].id,tempVar);
        }
    }
})
    .catch((error) => console.log('Hiba:', error));
}


function categoryList(){
    console.log("Loaded");
    fetch('http://localhost:5000/topics/types')
    .then(response => response.json())
    .then(data => { 
        for (let i = 0; i < data.length; i++) {
            let select = "<option value="+ data[i].id + ">"+ data[i].name + "</option>";
            document.getElementById('category').innerHTML+= select;
        }
    })
}

function getType(topicid, type_id=""){
    let vissza = "asd";
    fetch('http://localhost:5000/topics/type_id?type_id='+type_id)
    .then(response => response.text())
    .then(data => {
        let mes = "Kategória: "+data;
        document.getElementById('type'+topicid).innerHTML = mes;
    });
}

