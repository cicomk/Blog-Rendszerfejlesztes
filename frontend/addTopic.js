function hozzaad(){
    var cim = document.getElementById('cim').value
    var type = document.getElementById('category').value
    var szoveg = document.getElementById('szoveg').value
    let ujTema = {
        "name" : cim,
        "type_id" : type,
        "description" : szoveg
    };
    
    fetch('http://localhost:5000/topics/append', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(ujTema),
    })
    .then(response => console.log("ok"))
    .then(data => console.log(data))
    .catch((error) => console.error('Hiba:', error));
}
