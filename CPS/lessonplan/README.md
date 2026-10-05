# Teacher_Instructional_Design Dataset

## Overview
This dataset contains the Instructional Design, a dataset focused on analyzing teacher behavior in educational settings. The data is specifically geared toward understanding and evaluating teachers' instructional planning and design processes.

The dataset includes anonymized documents, transcripts, and annotations to ensure privacy while enabling AI-driven analysis and model training for educational applications.

## Purpose
The primary goal of this dataset is to facilitate research and development in educational AI, particularly in:
- Analyzing instructional design quality.
- Generating or evaluating lesson plans.
- Fine-tuning models for tasks like automated feedback on teaching materials.

## Dataset Structure and Contents
The folder includes the following files and subfolders:

### Files:
- **Multiple .docx files**: These are Word documents representing teacher-created instructional designs or lesson plans.  Each file typically contains detailed plans for classroom sessions, including objectives, activities, assessments, and materials.  The exact number and names may vary, but they are sourced from real teaching scenarios.

- **speech_text.xlsx**: An Excel spreadsheet containing transcribed texts from teacher lectures or speeches.  Columns may include timestamps, speaker identifiers, and the transcribed content, useful for aligning audio data with textual analysis.

- **instruction_design_anno.xlsx**: An annotated Excel file for instructional designs.  This includes labels, scores, or annotations on various aspects of the designs, such as clarity, engagement, alignment with learning objectives, and pedagogical effectiveness.  It serves as ground truth for supervised learning tasks.