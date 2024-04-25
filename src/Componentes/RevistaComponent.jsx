
const RevistaComponent=({imagen,titulo,descripcion})=>{

    return(
        <div style={{color: 'black'}}>
            <img src={imagen} alt="no carga imagen" style={{height:'450px', width:'auto'}}/>
            <h2>{titulo}</h2>
            <p style={{color: 'black'}}>{descripcion}</p>
        </div>
    )
}

export default RevistaComponent;