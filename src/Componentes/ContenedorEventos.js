const ContenedorEventos=({eventos})=>{
    return(
        <div class="image-container">
    {eventos.map((evento)=>(
    <div class="image-item">
        <img src={evento.foto} alt="Image" class="image"></img>
        <div class="image-text">
            <div class="image-title">{new DOMParser().parseFromString(evento.titulo, "text/xml")}</div>
            <div class="image-paragraph">{new DOMParser().parseFromString(evento.descripcion, "text/xml")}</div>
        </div>
    </div>))}
</div>
    )
}

export default ContenedorEventos;