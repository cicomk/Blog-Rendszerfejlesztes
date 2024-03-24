fetch('http://localhost:5000/api')
.then(response => response.text())
.then(data => {
    //console.log(data);
});

function list(topicId = ''){
    fetch('http://localhost:5000/topics?param='+topicId)
    .then(response => response.json())
    .then(data => {
        let mes = ""
        for (let i = 0; i < data.length; i++) {
            // Létrehozunk egy új div elemet
            
            let div = "<div id='" + data[i].id + "'>";
            div+="<h1>" + data[i].name + "</h1><h6>Kategória: " + data[i].type_id + "</h6><p>" + data[i].description +"</p><hr></div>"
            //div.textContent = `ID: ${data[i].id}, Név: ${data[i].name}, Típus ID: ${data[i].type_id}, Leírás: ${data[i].description}`;
        
            // Hozzáadjuk a div elemet a dokumentum testéhez
            mes+=div;
            //console.log(div);
        }
        document.getElementById('message').innerHTML = mes;
        //console.log(data)
    })
    .catch((error) => console.log('Hiba:', error));
}

