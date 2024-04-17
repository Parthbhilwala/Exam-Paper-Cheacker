import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavgBar from './Components/NavgBar';
import Banner from './Pages/Banner';
import Signup from './Pages/Signup';
import Login from './Pages/Login';
import User from './Pages/User';
import './Pages/User.css';
import Upload from './Pages/Upload';
import Uploadmcq from './Upload pages/Uploadmcq';
import Uploadfb from './Upload pages/Uploadfb';
import Uploadoneword from './Upload pages/Uploadoneword';
import Uploadmatch from './Upload pages/Uploadmatch';
import Score from './Upload pages/Score';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import About from './Pages/About_p';

function App() {
  let routes = (
    <Routes>
      {/* Specify the route path and the corresponding component */}
      <Route path="/" element={<Banner /> } />
      <Route path="/signup" element={<Signup />} />
      <Route path="/login" element={<Login />} />
      <Route path="/user/:userId" element={<User />} />
      <Route path="/upload" element={<Upload />} />
      <Route path="/upload/uploadmcq" element={<Uploadmcq />} />
      <Route path="/upload/uploadfb" element={<Uploadfb />} />
      <Route path="/upload/uploadoneword" element={<Uploadoneword />} />
      <Route path="/upload/uploadmatch" element={<Uploadmatch />} />
      <Route path="/upload/score" element={<Score />} />
      {/* <Route path="/uploadanswer" element={<Uploadsample />} /> */}
      {/* <Route path="/auth" element={<Auth />} />
        <Route path="*" element={<Navigate to="/auth" replace />} /> */}
    </Routes>
  )
  return (
    <Router className="App">
      <main>
        {routes}
      </main>

    </Router>
  );
}

export default App;