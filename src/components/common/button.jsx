const Button = ({
  title,
  titleColor,
  bg,
  bgHover,
  hoverColor,
  onClick,
  padding,
  width,
  className,
  style,
}) => {
  return (
    <>
      <button
        onClick={onClick}
        className={
          className
            ? className
            : `w-full bg-dark_green text-white p-2 rounded-md  text-center`
        }
        style={style ? style :{width:width, padding:padding,backgroundColor:bg}}
      >
        {title}
      </button>
    </>
  );
};

export default Button;
