import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/landingPage/LandingPage";
import NotFound from "./pages/notFound/NotFound";
import HomePage from "./pages/home/HomePage";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="*" element={<NotFound />} />
        <Route path="Home" element={<HomePage />} />
      </Routes>
    </Router>
  );
}
