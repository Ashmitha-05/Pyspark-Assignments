from src.Question4 import util
 
 
def main():
 
    
    employee_df = util.read_json_dynamic(
        spark,
        "/Volumes/workspace/sona/s1/nested_json_file.json"
    )
 
    print("Original Data")
    display(employee_df)
 
   
    flat_df = util.flatten_df(employee_df)
 
    print("Flattened Data")
    display(flat_df)
 

    print("Original Record Count :", util.record_count(employee_df))
    print("Flattened Record Count :", util.record_count(flat_df))
 
    
    print("explode()")
    display(util.explode_demo(employee_df))
 
    print("explode_outer()")
    display(util.explode_outer_demo(employee_df))
 
    print("posexplode()")
    display(util.posexplode_demo(employee_df))
 
    filtered_df = util.filter_id(flat_df)
 
    print("Filtered Data")
    display(filtered_df)
 

    renamed_df = util.rename_columns_snake(filtered_df)
 
    print("Snake Case Columns")
    display(renamed_df)
 
 
    load_df = util.add_load_date(renamed_df)
 
    
    final_df = util.add_partition_columns(load_df)
 
    print("Final Data")
    display(final_df)
 
    spark.sql("CREATE DATABASE IF NOT EXISTS employee")
 
    
    util.write_partitioned_table(final_df)
 
    print("Question 4 Completed Successfully")
 
 
if __name__ == "__main__":
    main()
 

 
