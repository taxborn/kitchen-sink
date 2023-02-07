#![feature(let_chains)]
#![feature(variant_count)]

use std::collections::HashMap;

#[repr(usize)]
enum Semester {
    Fall2020,
    Spring2021,
    Summer2021,
    Fall2021,
    Spring2022,
    Summer2022,
    Fall2022,
    Spring2023,
    Summer2023,
    Fall2023,
    Spring2024,
}

fn construct_grade_map() -> HashMap<String, f32> {
    HashMap::from([
        ("A+".into(), 4.0),
        ("A".into(), 4.0),
        ("A-".into(), 3.67),
        ("B+".into(), 3.33),
        ("B".into(), 3.0),
        ("B-".into(), 2.67),
        ("C+".into(), 2.33),
        ("C".into(), 2.0),
        ("C-".into(), 1.67),
        ("D+".into(), 1.33),
        ("D".into(), 1.0),
        ("D-".into(), 0.67),
        ("F".into(), 0.0),
        ("P".into(), 0.0), // Pass does not count for GPA
    ])
}

// ("Class Name", (Semester Taken, Credits, Grade))
fn construct_classes_map<'a>() -> HashMap<&'a str, (Semester, u8, Option<String>)> {
    HashMap::from([
        // Fall 2020
        (
            "Intro to Programming",
            (Semester::Fall2020, 4, Some("A".into())),
        ),
        (
            "United States Government",
            (Semester::Fall2020, 4, Some("A".into())),
        ),
        ("Calculus II", (Semester::Fall2020, 4, Some("A".into()))),
        // Spring 2021
        ("Pop Music USA", (Semester::Spring2021, 3, Some("A".into()))),
        ("Calculus III", (Semester::Spring2021, 4, Some("A+".into()))),
        (
            "Intro to Math Software",
            (Semester::Spring2021, 3, Some("A".into())),
        ),
        (
            "Data Structures",
            (Semester::Spring2021, 4, Some("A".into())),
        ),
        ("Composition", (Semester::Spring2021, 4, Some("A".into()))),
        // Summer 2021
        (
            "Concepts of Fitness",
            (Semester::Summer2021, 2, Some("A".into())),
        ),
        (
            "Intro to Sociology",
            (Semester::Summer2021, 3, Some("A".into())),
        ),
        (
            "Linear Algebra I",
            (Semester::Summer2021, 4, Some("A".into())),
        ),
        // Fall 2021
        (
            "Fitness Activities",
            (Semester::Fall2021, 1, Some("P".into())),
        ),
        (
            "General Physics I",
            (Semester::Fall2021, 4, Some("A".into())),
        ),
        ("Algorithms", (Semester::Fall2021, 4, Some("A".into()))),
        ("Set Theory", (Semester::Fall2021, 4, Some("A".into()))),
        (
            "Differential Equations",
            (Semester::Fall2021, 4, Some("A-".into())),
        ),
        // Spring 2022
        (
            "Discrete Math I",
            (Semester::Spring2022, 4, Some("A".into())),
        ),
        (
            "HONOR Portfolio Development",
            (Semester::Spring2022, 1, Some("A".into())),
        ),
        (
            "Computer Architecture",
            (Semester::Spring2022, 4, Some("A".into())),
        ),
        (
            "Physical Geology",
            (Semester::Spring2022, 4, Some("A".into())),
        ),
        // Summer 2022
        (
            "Intro to Philosphy",
            (Semester::Summer2022, 3, Some("A".into())),
        ),
        // Fall 2022
        ("CS Project I", (Semester::Fall2022, 4, Some("A".into()))),
        (
            "Databases & Security",
            (Semester::Fall2022, 2, Some("A".into())),
        ),
        (
            "Programming Languages",
            (Semester::Fall2022, 2, Some("A+".into())),
        ),
        ("CS Seminar I", (Semester::Fall2022, 1, Some("A".into()))),
        ("Probs & Stats", (Semester::Fall2022, 4, Some("A".into()))),
        // Spring 2023
        ("CS Project II", (Semester::Spring2023, 4, None)),
        ("Operating Systems", (Semester::Spring2023, 2, None)),
        ("SE & Parallel Computing", (Semester::Spring2023, 2, None)),
        (
            "Algorithms & Computability",
            (Semester::Spring2023, 2, None),
        ),
        ("Leetcode Class", (Semester::Spring2023, 2, None)),
        ("CS Seminar II", (Semester::Spring2023, 1, None)),
        // Summer 2023
        ("N/A", (Semester::Summer2023, 0, None)),
        // Fall 2023 - Need 2 electives
        ("CS Project III", (Semester::Fall2023, 4, None)),
        ("CS Seminar III", (Semester::Fall2023, 1, None)),
        ("Discrete Math II", (Semester::Fall2023, 4, None)),
        // Spring 2024 - Need 2 electives
        ("CS Project IV", (Semester::Spring2024, 4, None)),
        ("CS Seminar IV", (Semester::Spring2024, 1, None)),
        ("HONR Portfolio Cap", (Semester::Spring2024, 1, None)),
    ])
}

fn main() {
    let grades = construct_grade_map();
    let classes = construct_classes_map();

    let mut total_credits = 0;
    let mut total_credits_taken = 0;
    let mut total_gpa_points: f32 = 0.0;
    let mut credit_distribution = [0; std::mem::variant_count::<Semester>()];

    classes.into_values().for_each(|class| {
        let semester = class.0 as usize;
        let credits = class.1;
        let letter_grade = class.2;

        total_credits += credits;
        credit_distribution[semester] += credits;

        // Check if we have a grade posted
        if let Some(grade) = letter_grade && &grade != "P" {
            total_credits_taken += credits;

            if let Some(value) = grades.get(&grade) {
                total_gpa_points += credits as f32 * value;
            }
        }
    });

    println!("So far, I have taken {total_credits_taken} credits.");
    println!("I have {total_credits} credits planned. (Requires at least 120 to graduate)");
    println!("\tGPA: {}", total_gpa_points / total_credits_taken as f32);
    println!("credit distribution:\t{credit_distribution:?}");
}
