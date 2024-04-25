import ContenedorICM from "../Componentes/ContenedoresICM";
import Navbar from "../Componentes/Navbar";
const Premios = () => { 
    const [elements,setElements]=React.useState([]);
    React.useEffect(()=>{
        http.get('entidades/efemerides/')
        .then(response => {
          console.log(response.data);
          setElements(response.data);
        })
        .catch(error => {
          console.error('Error fetching (efemerides)', error);
        });
    },
    [])
    
    
    return (
        <div>
        <Navbar/>

        {elements.map((element)=>(
            <ContenedorICM titulo={element.titulo} encabezado={element.encabezado} 
        descripcion={element.descripcion} imagen={element.foto} />
        ))}
        
        </div>
    );
}

export default Premios;