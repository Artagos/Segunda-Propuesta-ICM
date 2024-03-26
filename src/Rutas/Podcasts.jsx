import '../ComponentsCss/Podcasts.css';
import VideoPlayer from "../Componentes/VideoPlayer";
import Navbar from '../Componentes/Navbar';

const Podcasts = () => {    
    return (
        <div>
            <Navbar/>
            <div className='stack'>
                <VideoPlayer light={<img style={{width:'100px'}} src='https://example.com/thumbnail.png' alt='Thumbnail' />} url={"/podcasts/C1.2 - Ing Soft Especificacion de Requerimientos - Curso 2022 Ok.mp4"}/>
                <VideoPlayer light={<img src='https://example.com/thumbnail.png' alt='Thumbnail' />} url={"/podcasts/C1.2 - Ing Soft Especificacion de Requerimientos - Curso 2022 Ok.mp4"}/>   
                <VideoPlayer light={<img src='https://example.com/thumbnail.png' alt='Thumbnail' />} url={"/podcasts/C1.2 - Ing Soft Especificacion de Requerimientos - Curso 2022 Ok.mp4"}/>
            </div>
        </div>
    )
}

export default Podcasts;