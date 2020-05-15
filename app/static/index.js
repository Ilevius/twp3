const api_url = '/api/';

let mtypes = []
let selected_mtype = []

//                                      API CRUD first layer
class Api {
    static fetch(object_url) {
        return fetch(api_url+object_url, {method: 'get'}).then(res => res.json())
    }

    static fetch_one(object_url) {
        return fetch(api_url+object_url, {method: 'get'}).then(res => res.json())
    }

    static create(object_url, object) {
        return fetch(api_url+object_url, {
            method: 'post',
            body: JSON.stringify(object),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }).then( res => res.json() )
    }

    static update(object_url, object) {
        return fetch(api_url+object_url, {
            method: 'put',
            body: JSON.stringify(object),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }).then( res => res.json() )
    }

    static delete(object_url) {
        return fetch(api_url+object_url, {method: 'delete'}).then(res => res.json())
    }

}



function render_tree(object){
    // fetching of the object's content range
    content_objects = object.subs.map(i=>{Api.fetch_one(object.info.content+'/'+i)})
    // converting content into the string, PekyPcuR ))
    str_content = content_objects.map( i=>{render_tree(i)} ).join(' ')
    // generating of the output string
    return `
    <li>${object.name}
    <ul>${str_content}</ul>
    </li>`
}




const show_mtype = mtype => {
    return `
    <li>${mtype.name}</li>
    `
}

function renderMtypes(_mtypes = []) {
    const $mtypes = document.querySelector('#tree')

    if (_mtypes.length > 0) {
        $mtypes.innerHTML = _mtypes.map(elem => show_mtype(elem)).join(' ')

    } else {
        $mtypes.innerHTML = '<div>Пока нет метатэгов</div>'
    }
}

function createMtype() {
    const nameField = document.querySelector('#itemName')
    if(nameField.value == ''){alert('Имя не должно быть пустым')}
    else{
            const newMtype = {
                name: nameField.value
            }
        
            Api.create('metatypes', newMtype).then( () => {
                alert('Saved!')
                Api.fetch('metatypes').then(backendMtypes => {
                    mtypes = backendMtypes.concat()
                    renderMtypes(mtypes)
                })

                nameField.value = ''
            })    
        }
}

const render_editor_mtype = (selected ={}) => {
    document.querySelector('#editorheader').innerHTML = 'Создание нового метатэга'
    document.querySelector('#editor').innerHTML = `
    <div class="form-group">
    <label for="itemName">Имя</label>
    <input type="text" class="form-control" id="itemName" value="${selected.name}">
    <br>
    <button type="button" class="btn btn-success btn-sm" id = "saveMtype">Сохранить метатэг</button>
    </div>
    `
    document.querySelector('#saveMtype').addEventListener('click', createMtype)
}


document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelector('#newmtype').addEventListener('click', render_editor_mtype)
    Api.fetch('metatypes').then(backendMtypes => {
        mtypes = backendMtypes.concat()
        renderMtypes(mtypes)
    })
})


