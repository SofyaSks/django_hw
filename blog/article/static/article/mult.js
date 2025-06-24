
window.addEventListener(
    'load',
    Main
)

function Main(){
    let btn = document.querySelector('button')
    // только вручную можно адрес задавать?
    url_add = 'http://127.0.0.1:8000/article/table/'

    btn.addEventListener(
        'click',
        () => {
            
            let num = document.querySelector('input').valueAsNumber
            document.querySelector('input').value = ''

            fetch(url_add).then(
                (response)=>{
                    createTable(num)              
                    return response.text()
                }
            )

        }
    )

}

function createTable(num){
    oldtable = document.querySelector('.oldtable')
    if (oldtable){
        oldtable.remove()
    }
    
    table = document.createElement('table')
    table.setAttribute('class', 'oldtable')

    for (let i = 1; i <= num; i++) {
        tr = document.createElement('tr')
        for (let j = 1; j <= num; j++) {
            td = document.createElement('td')
            td.textContent = i * j
            tr.appendChild(td)
        }
        table.appendChild(tr)
             
    }

    document.body.appendChild(table)

}