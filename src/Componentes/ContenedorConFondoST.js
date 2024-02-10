import '../ComponentsCss/ContenedoresConFondoST.css'
const CCFST=({fondo,titulo})=>{
    return(
        <div class="containerFST" style={{background: 'url('+fondo+')'}}>
            <div class="contentFST">
                <div class="titleFST">
                {titulo}
                </div>
                </div>
        </div>
        )
}

export default CCFST;