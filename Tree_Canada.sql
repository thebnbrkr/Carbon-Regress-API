CREATE TABLE TREE_CANADA (
    eng_name CHAR(50),
    sci_name CHAR(50),
    oth_name CHAR(50),
        type CHAR(50),
       zero_a CHAR(1),	/*Boolean - Y: YES and N:No */
       zero_b CHAR(1),	/*Boolean - Y: YES and N:No */
        one_a CHAR(1),	/*Boolean - Y: YES and N:No */
        one_b CHAR(1),	/*Boolean - Y: YES and N:No */
        two_a CHAR(1),	/*Boolean - Y: YES and N:No */
  		two_b CHAR(1),	/*Boolean - Y: YES and N:No */
      three_a CHAR(1),	/*Boolean - Y: YES and N:No */
      three_b CHAR(1),	/*Boolean - Y: YES and N:No */
       four_a CHAR(1),	/*Boolean - Y: YES and N:No */
       four_b CHAR(1),	/*Boolean - Y: YES and N:No */
       five_a CHAR(1),	/*Boolean - Y: YES and N:No */
       five_b CHAR(1),	/*Boolean - Y: YES and N:No */
        six_a CHAR(1),	/*Boolean - Y: YES and N:No */
        six_b CHAR(1),	/*Boolean - Y: YES and N:No */
      seven_a CHAR(1),	/*Boolean - Y: YES and N:No */
      seven_b CHAR(1),	/*Boolean - Y: YES and N:No */
      eight_a CHAR(1),	/*Boolean - Y: YES and N:No */
      eight_b CHAR(1),	/*Boolean - Y: YES and N:No */
       nine_a CHAR(1),	/*Boolean - Y: YES and N:No */
       native CHAR(2),	/* Na: Native, Nl: Naturalized, and In:Introduced */
        kdom CHAR(50),  /* Kingdom */
      family CHAR(50),
       genus CHAR(50),
        ordr CHAR(50),	/* Order */
       clade CHAR(50),	
       ticker CHAR(5),	/* Unique identifier */
       edible CHAR(1), /*Boolean - Y: YES and N:No */
      PRIMARY KEY(ticker)
  )
