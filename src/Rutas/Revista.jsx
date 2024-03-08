import CCFST from "../Componentes/ContenedorConFondoST"
import CCF from "../Componentes/ContenedorConFondo"
import ContenedorICM from "../Componentes/ContenedoresICM"
import Navbar from "../Componentes/Navbar"
const Revista =()=>{
    return(<div>
        <Navbar seccion={"S_Revista"}/>
        <CCF colorTitulo={'orange'} fondo={"https://img.fotocommunity.com/blanco-y-negro-00969dcb-ed51-4dd4-81d8-6b6eb0f1dc2d.jpg?height=1080"} titulo={"Titulo generico"} descripcion={"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."}/>
        <CCFST titulo={'Empresas y Negocios'} fondo={'https://cdn.pixabay.com/photo/2024/01/26/23/53/building-8534894_1280.jpg'}/>
        <ContenedorICM colorTitulo={'black'} titulo={'HISTORIA'} encabezado={'lore ipsum amet'} 
        descripcion={'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. In egestas erat imperdiet sed. Dolor sit amet consectetur adipiscing elit ut aliquam. Id faucibus nisl tincidunt eget nullam. Pellentesque habitant morbi tristique senectus et netus et. Aliquet nec ullamcorper sit amet risus nullam eget felis eget. Rhoncus urna neque viverra justo nec ultrices dui sapien. At varius vel pharetra vel turpis nunc eget lorem. Turpis egestas integer eget aliquet. Facilisi cras fermentum odio eu feugiat pretium nibh. In egestas erat imperdiet sed euismod. Tortor id aliquet lectus proin nibh. Et tortor consequat id porta nibh venenatis cras sed. Nibh venenatis cras sed felis eget velit. Eu lobortis elementum nibh tellus molestie nunc non. Ullamcorper dignissim cras tincidunt lobortis feugiat vivamus. Sit amet purus gravida quis blandit turpis cursus. Turpis tincidunt id aliquet risus feugiat in. Nibh mauris cursus mattis molestie a iaculis.'} colorFondo={'black'} 
        colorBoton={'black'} colorLboton={'white'} colorLetra={'white'} imagen={'/images/event.jpeg'}/>
        </div>
    )
}
export default Revista