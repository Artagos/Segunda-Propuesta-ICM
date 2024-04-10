const ContenedorEventos=({eventos})=>{
    return(
        <div class="image-container">
    {eventos.map((evento)=>(
    <div class="image-item">
        <img src={evento.foto} alt="Image" class="image"></img>
        <div class="image-text">
            <div class="image-title">{evento.título}</div>
            <div class="image-paragraph">{evento.descripción}</div>
        </div>
    </div>))}
</div>
    )
}

export default ContenedorEventos;