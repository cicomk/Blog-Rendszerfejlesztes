fetch('http://localhost:5000/api')
.then(response => response.text())
.then(data => {});

function start(){
    if (checkCookie() == '1'){
        list();
        categoryList();
    } else {
        window.location.href = './login.html';
    }

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
            let div = "<div id='" + data[i].id + "'>";
            var tempVar = data[i].type_id;
            //console.log(getType(tempVar.toString()) );
            div+="<h1>" + data[i].name + "</h1><h6 id='type" + data[i].id + "'>Kategória: " + "</h6><p>" + data[i].description +"</p><button onclick='getComments("+data[i].id+")'>Hozzászólások</button><p id='hozzSum"+data[i].id+"'>Hozzászólások száma: 0</p><div class='hozzaszolasok' id='hozz"+ data[i].id +"'></div><hr></div>";
            document.getElementById('message').innerHTML+= div;
            getType(data[i].id,tempVar);
            getSumComments(data[i].id);
        }
    }
})
    .catch((error) => console.log('Hiba:', error));
}
function getSumComments(id){
    fetch('http://127.0.0.1:5000/comment/sum?topic_id='+id)
    .then(response => response.json())
    .then(data => { 
        console.log(data);
        document.getElementById('hozzSum'+ id).innerHTML= "Hozzászólások száma: "+data;
    })
}

function getComments(id){
    fetch('http://localhost:5000/comment?topic_id='+id)
    .then(response => response.json())
    .then(data => {
        document.getElementById('hozz'+ id).innerHTML = "";
        if (data.length == 0) {
            document.getElementById('hozz'+ id).innerHTML = "Nincs hozzászólás";
        } else {
        for (let i = 0; i < data.length; i++) {            
            let div = "<div id='h" + data[i].id + "'>";
            div+="<b><p id='name" + data[i].user_id + "'> hozzászólása:</p></b><p>" + data[i].body + "</p><i>" + data[i].timestamp +"</i><hr></div>";
            document.getElementById('hozz'+ id).innerHTML+= div;
            getUserById(data[i].user_id);
        }
       
    }
    document.getElementById('hozz'+ id).innerHTML+= "<br><button onclick='commentForm("+id+")'>Új hozzászólás</button><div id='commentF"+id+"'> </div>";
   // console.log(id);
    })
    .catch((error) => console.log('Hiba:', error));
}

function getUserById(user_id){
    fetch('http://localhost:5000/users/getName?user_id='+user_id)
    .then(response => response.text())
    .then(data => { 
        document.getElementById('name'+ user_id).innerHTML= data + " hozzászólása:";
        document.getElementById('name'+ user_id).id = "user"+user_id;
    })
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


function commentForm(id){
    document.getElementById('commentF'+ id).innerHTML = '<label>Hozászólás: <input type="text" name="" id="hozzaszolasSzovege'+id+'"><button onclick="addComment('+id+',true)">Hozzáad</button>';
}
function addComment(id,hideElement=false){
    var user_id = sessionStorage.getItem("id");
    var topic_id = String(id)
    var body = document.getElementById('hozzaszolasSzovege'+id).value
    let ujKoment = {
        "user_id" : user_id,
        "topic_id" : topic_id,
        "body" : body
    };
    
    fetch('http://localhost:5000/comment/append', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(ujKoment),
    })
    .then(response => {
        getComments(id);
        getSumComments(id);})
    .then(data => console.log(data))
    .catch((error) => console.error('Hiba:', error));
    console.log(ujKoment);

}

function checkCookie(){
    if (sessionStorage.getItem("id")==null){
        return '0'
    } else {
        return '1'
    }
}