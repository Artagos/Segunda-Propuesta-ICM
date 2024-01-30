import '../ComponentsCss/ContenedoresICM.css';
import { useViewport } from '../useViewport';
const ContenedorICM=()=>{
    const {width,height}=useViewport();
    var breakWidth= width<900
    console.log(width)
    return(
<div>
    {!breakWidth?<div class="event-container"><div class="inf-side">
        <div class="aux-inf-side">
            <div class="event-title">Historia</div>
            <div class="event-details">
                <h4 >Lorem ipsum dolor sit amet</h4>
                <p>Description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>
            </div>
        </div>
        <a href="#" class="buttonC">más</a>
    </div>
    <div class="img-side"><img src="event.jpeg" alt="rhcp"></img></div></div>:<div class="event-container"><div class="img-side"><img src="event.jpeg" alt="rhcp"></img></div><div class="inf-side">
        <div class="aux-inf-side">
            <div class="event-title">Historia</div>
            <div class="event-details">
                <h4 >Lorem ipsum dolor sit amet</h4>
                <p>Description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>
            </div>
        </div>
        <a href="#" class="buttonC">más</a>
    </div></div>
    }
</div>
    )
}

export default ContenedorICM;