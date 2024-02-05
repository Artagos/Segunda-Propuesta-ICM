import { Route,Routes, BrowserRouter} from "react-router-dom"
import Main from "../Rutas/Main"
import Revista from "../Rutas/Revista"
import Efemerides from "../Rutas/Efemerides"
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
        <Route  path={'Contactos'} element={<div class="contact-section">
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
} />
        <Route  path={'Eventos'} element={<div class="image-container">
    <div class="image-item">
        <img src="https://www.mexicodesconocido.com.mx/wp-content/uploads/2021/06/cultura-de-mexico-depositphotos.jpg" alt="Image 1" class="image"></img>
        <div class="image-text">
            <div class="image-title">Title 1</div>
            <div class="image-paragraph">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
        </div>
    </div>

    <div class="image-item">
        <img src="https://pymstatic.com/86302/conversions/tipos-de-cultura-social.jpg" alt="Image 2" class="image"></img>
        <div class="image-text">
            <div class="image-title">Title 2</div>
            <div class="image-paragraph">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
        </div>
    </div>
    <div class="image-item">
        <img src="https://www.mexicodesconocido.com.mx/wp-content/uploads/2021/06/cultura-de-mexico-depositphotos.jpg" alt="Image 1" class="image"></img>
        <div class="image-text">
            <div class="image-title">Title 1</div>
            <div class="image-paragraph">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
        </div>
    </div>
    <div class="image-item">
        <img src="https://pymstatic.com/86302/conversions/tipos-de-cultura-social.jpg" alt="Image 2" class="image"></img>
        <div class="image-text">
            <div class="image-title">Title 2</div>
            <div class="image-paragraph">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
        </div>
    </div>



</div>
} />
            
      </Routes>
      </BrowserRouter>
      </div>)
}
export default RoutesICM