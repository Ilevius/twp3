const api_url = '/api/';

let mtypes = []
let selected_mtype = []

//                                      Metatype's CRUD 
class Api {
    static fetch(object) {
        return fetch(api_url+object, {method: 'get'}).then(res => res.json())
    }

    static fetch_one(object, id) {
        return fetch(api_url+object+'/'+id, {method: 'get'}).then(res => res.json())
    }

    static create(object, Mtype) {
        return fetch(api_url+object, {
            method: 'post',
            body: JSON.stringify(Mtype),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }).then( res => res.json() )
    }

    static update(object, Mtype, id) {
        return fetch(api_url+object+'/'+id, {
            method: 'put',
            body: JSON.stringify(Mtype),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }).then( res => res.json() )
    }

    static delete(object, id) {
        return fetch(api_url+object+'/'+id, {method: 'delete'}).then(res => res.json())
    }

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


