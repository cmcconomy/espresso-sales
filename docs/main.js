async function getData() {
    let response = await fetch( './data/sales.json')
    let json = await response.json()

    // json.forEach((item) => {
    //     item.name = `<a href=${item.url}>${item.name}</a>`
    // })


    // debugger;
    return json
}

function autoSizeAll(gridOptions, skipHeader) {
  var allColumnIds = [];
  gridOptions.columnApi.getAllColumns().forEach(function (column) {
    allColumnIds.push(column.colId);
  });

  gridOptions.columnApi.autoSizeColumns(allColumnIds, skipHeader);
}

function currencyFormatter(value) {
  return `$${value.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',')}`
}

function percentFormatter(value) {
  return `${value.toFixed(2)}%`
}

async function setupTable() {
  const columnDefs = [
    { field: "image", resizable: true,
      cellRenderer: (row) => {
        return `<a href="${row.data.url}"><img style="height:40px" src="${row.data.image}" alt="${row.data.name}"</a>`
      }
    
    },
    { field: "name", sortable: true, filter: true, resizable: true },
    { field: "Sale Price", sortable: true, filter: true, resizable: true,
      valueGetter: (row) => {
        return row.data.sale_price
      },
      valueFormatter: (row) => {
        return currencyFormatter(row.value) 
      }
    },
    { field: "Original Price", sortable: true, filter: true, resizable: true,
      valueGetter: (row) => {
        return row.data.regular_price
      },
      valueFormatter: (row) => {
        return currencyFormatter(row.value) 
      }
    },
    { field: "Savings", sortable: true, filter: true, resizable: true,
      valueGetter: (row) => {
        return row.data.regular_price - row.data.sale_price
      },
      valueFormatter: (row) => {
        return currencyFormatter(row.value) 
      }
    },
    { field: "Savings (%)", sortable: true, filter: true, resizable: true,
      valueGetter: (row) => {
        return 100.0 * (row.data.regular_price - row.data.sale_price)/row.data.regular_price
      },
      valueFormatter: (row) => {
        return percentFormatter(row.value) 
      }
    },
    { field: "Site", sortable: true, filter: true, resizable: true,
      valueGetter: (row) => {
        return row.data.website
      }
    }

  ];
  
  // specify the data
  let rowData = await getData()
  const update_date = rowData.retrieved_at
  let date_placeholder = document.body.querySelector('#update_date')
  date_placeholder.innerText = update_date
  
  // let the grid know which columns and what data to use
  const gridOptions = {
    columnDefs: columnDefs,
    rowData: rowData.sale_items
  };

  const gridDiv = document.querySelector('#myGrid');
  new agGrid.Grid(gridDiv, gridOptions);

  var allColumnIds = [];
		gridOptions.columnApi.getAllColumns().forEach(function (column) {
      if( column.colId != 'name')
			  allColumnIds.push(column.colId);
		});

		gridOptions.columnApi.autoSizeColumns(allColumnIds);

  // // setup the grid after the page has finished loading
  // document.addEventListener('DOMContentLoaded', () => {
  //     const gridDiv = document.querySelector('#myGrid');
  //     new agGrid.Grid(gridDiv, gridOptions);
  // });


}

setupTable()