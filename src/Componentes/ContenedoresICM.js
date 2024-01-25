import '../ComponentsCss/ContenedoresICM.css';
const ContenedorICM=()=>{
    return(
<div className="event-container">
    <div className='inf-side'> 
        <div className='aux-inf-side'>          
            <div className="event-title">Historia</div>
            <div className="event-details">
            <h4 style={{textTransform:"uppercase",fontFamily: 'sans-serif'}}>Lorem ipsum dolor sit amet</h4>

            <p>Description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>
            </div>
        </div>
    </div>
    <div className='img-side'><img src='event.jpeg' alt='rhcp'></img></div>
</div>
    )
}

export default ContenedorICM;