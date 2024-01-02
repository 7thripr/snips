//A fast inverse squaroot operation from the quake 3 game engine written in RUST

fn inv_sqrt(x: f32) -> f32 {
    let xhalf = 0.5 * x;
    let i = x.to_bits() as i32;
    let i = 0x5f3759df - (i >> 1);
    let mut x = f32::from_bits(i as u32);
    x *= 1.5 - xhalf * x * x;
    x
}

fn main() {
    println!("{}", inv_sqrt(1.0));
}
