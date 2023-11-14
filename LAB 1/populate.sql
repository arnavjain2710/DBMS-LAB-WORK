use  eurekadb;

INSERT INTO employee(employee_name, street, city, join_date) 
VALUES
  ('Amit Agarwal', '123 Main Street', 'Bangalore', '2020-01-01'),
  ('Atul Gupta', '456 Elm Street', 'Chennai', '2020-02-01'),
  ('Bhaskar Joshi', '789 Oak Street', 'Mumbai', '2020-03-01'),
  ('Chandan Kumar', '1011 Pine Street', 'Kolkata', '2020-04-01'),
  ('Deepak Mishra', '1213 Maple Street', 'New Delhi', '2020-05-01'),
  ('Ekta Sharma', '1415 Oak Street', 'Pune', '2020-06-01'),
  ('Farhan Khan', '1617 Pine Street', 'Hyderabad', '2020-07-01'),
  ('Gaurav Kapoor', '1819 Maple Street', 'Ahmedabad', '2020-08-01'),
  ('Harsh Mehta', '2021 Oak Street', 'Jaipur', '2020-09-01'),
  ('Ishita Rastogi', '2223 Pine Street', 'Lucknow', '2020-10-01'),
  ('Jatin Srivastava', '2425 Maple Street', 'Kanpur', '2020-11-01'),
  ('Karan Taneja', '2627 Oak Street', 'Patna', '2020-12-01'),
  ('Lalit Verma', '2829 Pine Street', 'Bhopal', '2021-01-01'),
  ('Mansi Wadhwa', '3031 Maple Street', 'Indore', '2021-02-01'),
  ('Nikhil Arora', '3233 Oak Street', 'Nagpur', '2021-03-01'),
  ('Om Prakash', '3435 Pine Street', 'Aurangabad', '2021-04-01'),
  ('Priyanka Singh', '3637 Maple Street', 'Nashik', '2021-05-01'),
  ('Rajat Tiwari', '3839 Oak Street', 'Amritsar', '2021-06-01'),
  ('Sahil Sharma', '4041 Pine Street', 'Jodhpur', '2021-07-01'),
  ('Tanmay Gupta', '4243 Maple Street', 'Jaisalmer', '2021-08-01'),
  ('Utkarsh Jain', '4445 Oak Street', 'Bikaner', '2021-09-01');




INSERT INTO department(department_name, city) 
VALUES
('IT', 'Bangalore'),
('HR', 'Chennai'),
('Finance', 'Mumbai'),
('Sales', 'Kolkata');

INSERT INTO works(employee_name, department_name, job_title, annual_salary, notes) 
VALUES
('Amit Agarwal', 'IT', 'Software Engineer', 100000, 'Leads the development of new software products'),
('Atul Gupta', 'HR', 'Manager', 150000, 'Manages the HR department'),
('Bhaskar Joshi', 'Finance', 'CFO', 80000, "Manages the company's finances"),
('Chandan Kumar', 'Sales', 'Sales Representative', 60000, 'Generates new sales leads');

INSERT INTO manages(employee_name, manager_name) 
VALUES
  ('Amit Agarwal', 'Lalit Verma'),
  ('Atul Gupta', 'Priyanka Singh'),
  ('Bhaskar Joshi', 'Nikhil Arora'),
  ('Chandan Kumar', 'Om Prakash'),
  ('Deepak Mishra', 'Rajat Tiwari'),
  ('Ekta Sharma', 'Mansi Wadhwa'),
  ('Farhan Khan', 'Sahil Sharma'),
  ('Gaurav Kapoor', 'Utkarsh Jain');














