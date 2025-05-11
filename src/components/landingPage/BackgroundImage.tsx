interface BackgroundImageProps {
  image: string;
}

export default function BackgroundImage({ image }: BackgroundImageProps) {
  return (
    <div
      className="absolute top-0 left-0 w-full h-full bg-center z-0 transition-all duration-1500 ease-in-out"
      style={{
        backgroundImage: `url(${image})`,
        backgroundPosition: "center center",
        backgroundSize: "contain",
        backgroundRepeat: "no-repeat",
      }}
    />
  );
}
