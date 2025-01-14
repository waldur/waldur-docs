# Table component

1. State management is done via `useTable` React hook.
2. Table rendering is done using `Table` component.

```ts
import { translate } from '@waldur/i18n';
import Table from '@waldur/table/Table';
import { createFetcher } from '@waldur/table/api';
import { useTable } from '@waldur/table/useTable';

export const RolesList = () => {
  const tableProps = useTable({
    table: `RolesList`,
    fetchData: createFetcher('roles'),
  });

  return (
    <Table
      {...tableProps}
      columns={[
        {
          title: translate('Name'),
          render: ({ row }) => row.name,
        },
        {
          title: translate('Description'),
          render: ({ row }) => row.description,
        },
        {
          title: translate('Assigned users count'),
          render: ({ row }) => row.users_count,
        },
      ]}
    />
  );
};
```

Column definition consists of two mandatory fields: `title` and `render`.

## fetchData property

The fetchData property is a function that retrieves data for the table. It should return a promise that resolves to an object containing rows and resultCount. The `fetchData` function can be customized to fetch data from any API endpoint and transform it as needed before passing it to the table.

Example:

```ts
const fetchData = () => Promise.resolve({
  rows: resource.items,
  resultCount: resource.items.length,
});
```

## Export feature

Table component supports data export functionality. To enable it:

1. Add `enableExport` prop to the Table component
2. Configure export options in column definitions:

```ts
{
  title: 'Name',
  render: ({ row }) => row.name,
  export: 'name' // Use field directly
}

{
  title: 'Status',
  render: ({ row }) => row.status,
  export: row => formatStatus(row.status) // Custom formatter
}

{
  title: 'Actions',
  render: ({ row }) => <Button/>,
  export: false // Exclude from export
}
```

Optionally, specify `exportTitle` property for columns to customize the header in the exported file:

```ts
{
  title: 'Name',
  render: ({ row }) => row.name,
  export: 'name',
  exportTitle: 'User Name' // Custom header for export
}
```

## Optional columns

Table component supports optional columns that can be toggled by users. Optional columns allow users to customize their view by showing/hiding specific columns.

1. Add `hasOptionalColumns` prop to enable optional columns functionality
2. Configure columns with:

    - `id` - unique column identifier
    - `keys` - defines which fields should be requested from API (allows optimization by fetching only needed fields)
    - `optional` - mark column as optional to allow toggling

3. For actions column, you can specify mandatory fields that should always be fetched from API using `mandatoryFields` prop.

Example:

```ts
export const UsersTable = () => {
  const tableProps = useTable({
    table: 'users',
    fetchData: createFetcher('users'),
  });

  return (
    <Table
      {...tableProps}
      hasOptionalColumns
      mandatoryFields={['uuid', 'name']}
      columns={[
        {
          id: 'name',
          title: translate('Name'),
          render: ({ row }) => row.name,
          optional: true,
          keys: ['name'],
        },
        {
          id: 'email',
          title: translate('Email'),
          render: ({ row }) => row.email,
          optional: true,
          keys: ['email'],
        },
        {
          id: 'role',
          title: translate('Role'),
          render: ({ row }) => row.role,
          optional: true,
          keys: ['role', 'permissions'],
        },
      ]}
    />
  );
};
```

## Ordering feature

Table component supports column ordering. To enable it:

1. Add `enableOrdering` prop to the Table component
2. Configure columns with `orderField` property to specify which field should be used for ordering

Example:

```ts
export const UsersTable = () => {
  const tableProps = useTable({
    table: 'users',
    fetchData: createFetcher('users'),
  });

  return (
    <Table
      {...tableProps}
      enableOrdering
      columns={[
        {
          title: translate('Name'),
          render: ({ row }) => row.name,
          orderField: 'name',
        },
        {
          title: translate('Email'),
          render: ({ row }) => row.email,
          orderField: 'email',
        },
      ]}
    />
  );
};
```

When ordering is enabled, clicking on column headers will toggle between ascending and descending order.

## Filters feature

Filters are defined using the `filters` prop of the Table component. This prop accepts a React component that renders the filter UI.

Example:

```ts
import { useSelector } from 'react-redux';
import { getFormValues } from 'redux-form';

const getFilterValues = getFormValues('FilterForm');

export const FilterSet = () => (
  <TableFilterItem title="Filter field" name="custom">
    <Field name="custom" component="input" />
  </TableFilterItem>
);

export const FilteredList = () => {
  const filter = useSelector(getFilterValues);
  const tableProps = useTable({
    table: 'FilteredList',
    fetchData: createFetcher('hooks'),
    filter,
  });

  return (
    <Table
      {...tableProps}
      filters={<FilterSet />}
    />
  );
};
```

### Inline filters

The feature allows users to quickly filter table data by clicking values directly in the table cells, without manually setting filters. When column has `inlineFilter` property enabled:

1. A filter icon appears when hovering over cells in that column
2. Clicking the icon adds a filter using the cell's value
3. The `inlineFilter` function transforms row data into the filter value format

Example:

```ts
{
  title: translate('Organization'),
  render: ({ row }) => row.customer_name,
  filter: 'organization',  // Enable filtering
  inlineFilter: (row) => ({
    // Transform row data into filter value
    name: row.customer_name,
    uuid: row.customer_uuid
  })
}
```

## Grid mode

Table component supports switching between table and grid views. In grid mode, data is displayed as cards in a responsive grid layout.

To enable grid mode:

1. Add `gridItem` prop to specify the component used to render each item in grid view
2. Optionally customize grid layout using `gridSize` prop which accepts Bootstrap column properties
3. Set `initialMode` to 'grid' if you want grid view by default (table view is default)

Example:

```ts
export const GridListItem = ({ row }) => (
  <Card>
    <CardHeader>{row.name}</CardHeader>
    <CardBody>
      <p>{row.description}</p>
      <small>Users: {row.users_count}</small>
    </CardBody>
  </Card>
);

export const GridList = () => {
  const tableProps = useTable({
    table: 'GridList',
    fetchData: createFetcher('items'),
  });

  return (
    <Table
      {...tableProps}
      gridItem={GridListItem}
      gridSize="col-sm-6 col-md-4"
      initialMode="grid"
    />
  );
};
```
