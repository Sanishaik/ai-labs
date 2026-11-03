REPORT ZSS_PO_OPEN_LIST.
*---------------------------------------------------------------------*
* 1. LOCAL CLASS DEFINITION
*---------------------------------------------------------------------*
CLASS lcl_po_report DEFINITION.
  PUBLIC SECTION.
    METHODS get_data.
  PRIVATE SECTION.
    METHODS display_alv.
ENDCLASS.
*---------------------------------------------------------------------*
* 2. TYPES
*---------------------------------------------------------------------*
TYPES: BEGIN OF ty_po,
         ebeln TYPE ekko-ebeln,
         ebelp TYPE ekpo-ebelp,
         bedat TYPE ekko-bedat,
         lifnr TYPE ekko-lifnr,
         name1 TYPE lfa1-name1,
         matnr TYPE ekpo-matnr,
         txz01 TYPE ekpo-txz01,
         werks TYPE ekpo-werks,
         menge TYPE ekpo-menge,
         meins TYPE ekpo-meins,
         netwr TYPE ekpo-netwr,
         waers TYPE ekko-waers,
       END OF ty_po.
*---------------------------------------------------------------------*
* 3. INTERNAL TABLE AND OBJECT REFERENCES
*---------------------------------------------------------------------*
DATA: gt_po        TYPE TABLE OF ty_po,
      gv_ebeln     TYPE ekko-ebeln,
      gv_lifnr     TYPE ekko-lifnr,
      gv_bedat     TYPE ekko-bedat,
      gv_werks     TYPE ekpo-werks,
      go_salv      TYPE REF TO cl_salv_table,
      go_po_report TYPE REF TO lcl_po_report.
*---------------------------------------------------------------------*
* 4. SELECTION SCREEN
*---------------------------------------------------------------------*
SELECTION-SCREEN BEGIN OF BLOCK b1 WITH FRAME TITLE text-001.
  SELECT-OPTIONS: s_ebeln FOR gv_ebeln,
                  s_lifnr FOR gv_lifnr,
                  s_bedat FOR gv_bedat,
                  s_werks FOR gv_werks.
SELECTION-SCREEN END OF BLOCK b1.
*---------------------------------------------------------------------*
* 5. LOCAL CLASS IMPLEMENTATION
*---------------------------------------------------------------------*
CLASS lcl_po_report IMPLEMENTATION.
  METHOD get_data.
    CLEAR gt_po.
    SELECT a~ebeln,
           b~ebelp,
           a~bedat,
           a~lifnr,
           c~name1,
           b~matnr,
           b~txz01,
           b~werks,
           b~menge,
           b~meins,
           b~netwr,
           a~waers FROM ekko AS a
                   INNER JOIN ekpo AS b
                   ON b~ebeln = a~ebeln
                   LEFT OUTER JOIN lfa1 AS c
                   ON c~lifnr = a~lifnr
                   WHERE a~ebeln IN @s_ebeln
                   AND a~lifnr IN @s_lifnr
                   AND a~bedat IN @s_bedat
                   AND b~werks IN @s_werks
                  INTO CORRESPONDING FIELDS OF TABLE @gt_po.
    IF gt_po IS NOT INITIAL.
      display_alv( ).
    ELSE.
      MESSAGE 'No purchase order items found' TYPE 'S'.
    ENDIF.
  ENDMETHOD.

  METHOD display_alv.
    TRY.
        CALL METHOD cl_salv_table=>factory
          IMPORTING
            r_salv_table = go_salv
          CHANGING
            t_table      = gt_po.
        go_salv->get_functions( )->set_all( abap_true ).
        go_salv->get_columns( )->set_optimize( abap_true ).
        go_salv->get_display_settings( )->set_list_header('Open Purchase Order List' ).
        go_salv->display( ).
      CATCH cx_salv_msg INTO DATA(lx_salv).
        MESSAGE lx_salv->get_text( ) TYPE 'E'.
    ENDTRY.
  ENDMETHOD.
ENDCLASS.
*---------------------------------------------------------------------*
* 6. START-OF-SELECTION
*---------------------------------------------------------------------*
START-OF-SELECTION.
  CREATE OBJECT go_po_report.
  go_po_report->get_data( ).







