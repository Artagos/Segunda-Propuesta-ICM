import ContenedorICM from "../Componentes/ContenedoresICM";
import CCF from "../Componentes/ContenedorConFondo";
import CCFST from "../Componentes/ContenedorConFondoST";




export function MiniParser(data){
    if(data.tipo_contenedor==="ContenedorConFondo"){
        return(
            <CCF titulo={data.titulo} descripcion={data.descripcion} fondo={'/'+data.foto} />
        )
    }
    else if(data.tipo_contenedor==="ContenedorConFondoSoloTitulo"){
        return(
            <CCFST fondo={'/'+data.foto} titulo={data.titulo}/>
        )
    }
    
    else if(data.tipo_contenedor==="ContenedorICM"){
        return(
            <ContenedorICM titulo={data.titulo} encabezado={data.encabezado} descripcion={data.descripcion} 
            imagen={'/'+data.foto} colorFondo={data.color_de_fondo} colorLetra={data.color_de_letra} 
            colorBoton={data.color_boton} colorLBoton={data.color_letra_boton}/>
        )
    }

    
    return(null)
}