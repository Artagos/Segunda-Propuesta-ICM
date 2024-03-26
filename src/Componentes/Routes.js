import { Route,Routes, BrowserRouter} from "react-router-dom"
import Main from "../Rutas/Main"
import Revista from "../Rutas/Revista"
import Efemerides from "../Rutas/Efemerides"
import Eventos from "../Rutas/Eventos"
import Navbar from "./Navbar"
import Podcasts from "../Rutas/Podcasts"
const RoutesICM=()=>{
    return(<div>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={ <Main/>} />
        <Route  path={'QuienesSomos'} element={''} />
        <Route  path={'Efemerides'} element={<Efemerides/>} />
        <Route  path={'PremioNacionalMusica'} element={''} />
        <Route  path={'Novedades'} element={''} />
        <Route  path={'Multimedios'} element={''} />
        <Route  path={'Revista'} element={<Revista/>} />
        <Route  path={'Podcasts'}  element={<Podcasts/>}/>
        <Route  path={'Contactos'} element={
<div>
    <Navbar/>
        <div class="contact-section">
            
    <div class="contact-info">
        <p><span class="leader">CEO:</span> John Doe</p>
        <p><span class="leader">Email:</span> john.doe@example.com</p>
        <p><span class="leader">Phone:</span> +1 (555) 123-4567</p>
    </div>

    <div class="contact-info">
        <p><span class="leader">CTO:</span> Jane Smith</p>
        <p><span class="leader">Email:</span> jane.smith@example.com</p>
        <p><span class="leader">Phone:</span> +1 (555) 987-6543</p>
    </div>

    
    </div>
</div>
} />
        <Route  path={'Eventos'} element={<Eventos/>}/>
            
      </Routes>
      </BrowserRouter>
      </div>)
}
export default RoutesICM