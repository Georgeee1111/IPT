interface SlideTextProps {
  title: string;
  description: string;
}

export default function SlideText({ title, description }: SlideTextProps) {
  return (
    <div className="flex flex-col justify-center items-start max-w-lg">
      <h1 className="text-lg tracking-widest mb-2">lorem ipsum</h1>
      <h2 className="text-5xl font-bold">lorem ipsum</h2>
      <h3 className="text-4xl font-bold text-orange-500 mt-2">
        {title.toUpperCase()}
      </h3>
      <p className="max-w-xl mt-4 text-gray-200">{description}</p>
      <div className="mt-6 flex gap-4">
        <button className="border px-4 py-2 hover:bg-white hover:text-black transition">
          SEE MORE
        </button>
        <button className="border px-4 py-2 bg-white text-black hover:bg-transparent hover:text-white transition">
          SUBSCRIBE
        </button>
      </div>
    </div>
  );
}
