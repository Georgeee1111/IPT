import Navbar from "../../components/general/Navbar";
import { brandLogo } from "../../config/brandConfig";

function HomePage() {
  return (
    <>
      <Navbar logo={brandLogo} showSearch={true} />

      <main className="pt-24 px-6 text-white min-h-screen bg-gray-900">
        <h1 className="text-3xl font-bold mb-4">Home Page</h1>
      </main>
    </>
  );
}

export default HomePage;
