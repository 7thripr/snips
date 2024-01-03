// 1. Render any list to html be it string or nums the rendered result is a always string
pub fn list_to_html<T: ToString>(list: &[T]) -> Vec<Html> {
    list.iter().map(|item| html! {<li>{item.to_string()}</li>}).collect()
}

fn main {
println!("Snaps");
}
