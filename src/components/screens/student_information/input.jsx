const Input = ({
  className,
  label,
  placeholder,
  type,
  direction,
  align,
  marginTop,
  justify,
  items,
}) => {
  return (
    <>
      <div
        className={`w-full flex ${direction ? direction : "flex-col"}  ${
          items ? items : ""
        } ${justify ? justify : ""}`}
      >
        <label
          className={`text-sm text-brown  font-medium ${align ? align : "text-left"} ${
            marginTop ? marginTop : ""
          }`}
        >
          {label}
        </label>
        <input className={className} placeholder={placeholder} type={type} />
      </div>
    </>
  );
};

export default Input;
