import { Link } from "react-router-dom";

const NotFound = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-900 text-white text-center px-4">
      <h1 className="text-6xl font-bold mb-4">404</h1>
      <p className="text-xl mb-6">
        Oops! The page you’re looking for doesn’t exist.
      </p>
      <Link
        to="/"
        className="bg-white text-gray-900 px-6 py-3 rounded-full font-medium hover:bg-gray-200 transition duration-300"
      >
        Go Back Home
      </Link>
    </div>
  );
};

export default NotFound;
