import LoginPage from "./pages/LoginPage";
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter,Routes,Route,} from "react-router-dom";
import {AuthProvider} from './context/authcontext'
import HomePage from "./pages/HomePage";
import RegisterPage from "./pages/RegisterPage";
import VerifyPage from "./pages/VerifyPage";
import ForgotPage from "./pages/ForgotPage";
import PosingJobPage from "./pages/PosingJobPage";
import LoginProtect from "./PrivetRouters/LoginProtect";
import CaseOfReverse from "./PrivetRouters/CaseOfReverse";
import JobHomePage from "./pages/JobHomePage";
import Payment from "./components/Payment";


function App() {
  return (
    // <div >
      <>

     

      <BrowserRouter>
        <AuthProvider>
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route element={<CaseOfReverse />}>
               
                <Route path="/login" element={<LoginPage />} />
                <Route path="/register" element={<RegisterPage />} />
                <Route path="/verify" element={<VerifyPage />}/> 
                <Route path='/forgot_password' element={<ForgotPage/>}/>  
              </Route>
              <Route element={<LoginProtect/>}>
                <Route path="/postjob" element={<PosingJobPage />} />  
                <Route path='/jobhome' element={<JobHomePage />}/>    
                <Route path='/payment' element={<Payment />}/>               
              </Route>    
            </Routes>
        </AuthProvider>
      </BrowserRouter>    
        
      </>
    // {/* </div> */}
  );
}

export default App;
