import ReactPlayer from "react-player";
import React from "react";


const VideoPlayer = ({url,light}) => {
    
    return (
        <div style={{textAlign: 'center',
            padding: '20px',
            margin: '5px',}}>
                <div class="event-title" style={{color:'black'}} >Titulo por defecto</div>
                        <div class="event-details" >
                            
                            <p style={{color:'black'}}> Lore ipsum amet dolor sigmund dore anime simet factum cemu</p>
                        </div>
            <ReactPlayer url={url} style={{border: '2px solid #333'}} light={light} controls={true} />
        </div>
    )
}

export default VideoPlayer;