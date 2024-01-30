import { Route,Routes, BrowserRouter} from "react-router-dom"
import Main from "../Rutas/Main"
import Revista from "../Rutas/Revista"
const RoutesICM=()=>{
    return(<div>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={ <Main/>} />
        <Route  path={'QuienesSomos'} element={''} />
        <Route  path={'Efemerides'} element={''} />
        <Route  path={'PremioNacionalMusica'} element={''} />
        <Route  path={'Novedades'} element={''} />
        <Route  path={'Multimedios'} element={''} />
        <Route  path={'Revista'} element={<Revista/>} />
        <Route  path={'Contactos'} element={''} />
        <Route  path={'Eventos'} element={''} />
            
      </Routes>
      </BrowserRouter>
      </div>)
}
export default RoutesICM