use std::ffi::CStr;
use std::os::raw::c_char;

unsafe fn unpack_str(str_ptr: *const c_char) {
    let bytes = CStr::from_ptr(str_ptr).to_bytes();
    std::str::from_utf8(bytes).unwrap();
}

#[no_mangle]
pub extern "C" fn name(str_ptr: *const c_char) {
    //the result should be a pointer to an array of bytes, where each byte represents a ascii character
    unsafe {
        let bytes = CStr::from_ptr(str_ptr).to_bytes();
        let x = std::str::from_utf8(bytes).unwrap();

        println!("{}", x);
    };
}
