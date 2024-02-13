import CCFST from "../Componentes/ContenedorConFondoST"
import ContenedorICM from "../Componentes/ContenedoresICM"
const Revista =()=>{
    return(<div>
        <CCFST titulo={'Empresas y Algo ahi'} fondo={'https://cdn.pixabay.com/photo/2024/01/26/23/53/building-8534894_1280.jpg'}/>
        <ContenedorICM titulo={'HISTORIA'} encabezado={'lore ipsum amet'} 
        descripcion={'bbbbdfnsjnhbobbsdhfbabubuybsdhjhbbswd'} colorFondo={'orange'} 
        colorBoton={'white'} colorLboton={'black'} colorLetra={'white'} imagen={'https://cdn.pixabay.com/photo/2024/01/26/23/53/building-8534894_1280.jpg'}/>
        </div>
    )
}
export default Revista