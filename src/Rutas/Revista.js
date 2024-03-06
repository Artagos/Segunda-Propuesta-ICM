import CCFST from "../Componentes/ContenedorConFondoST"
import CCF from "../Componentes/ContenedorConFondo"
import ContenedorICM from "../Componentes/ContenedoresICM"
const Revista =()=>{
    return(<div>
        <CCFST titulo={'Empresas y Algo ahi'} fondo={'https://cdn.pixabay.com/photo/2024/01/26/23/53/building-8534894_1280.jpg'}/>
        <ContenedorICM titulo={'HISTORIA'} encabezado={'lore ipsum amet'} 
        descripcion={'bbbbdfnsjnhbobbsdhfbabubuybsdhjhbbswd'} colorFondo={'orange'} 
        colorBoton={'white'} colorLboton={'black'} colorLetra={'white'} imagen={'https://cdn.pixabay.com/photo/2024/01/26/23/53/building-8534894_1280.jpg'}/>
        <CCF fondo={"/images/Captura_de_pantalla_2024-02-29_163211_xULR6dW.png"} titulo={"Candela"} descripcion={"tengo problemas en el gao"}/>
        </div>
    )
}
export default Revista