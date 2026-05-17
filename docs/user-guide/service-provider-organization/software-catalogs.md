# Software Catalogs

Software catalogs allow service providers to associate scientific software environments
(such as EESSI or Spack) with their HPC and AI/ML offerings. End users can then browse
available software packages, versions, and compatible hardware targets directly from the
offering page.

## Associating a catalog with an offering

To link a software catalog to an offering:

1. Navigate to **Provider dashboard** > **Offerings** and select the offering.
2. Open the **Software catalogs** tab.
3. Click **Add** and select a catalog from the dropdown.
4. Configure the **CPU family** filter (e.g., `x86_64`, `aarch64`) to limit which
   targets are shown to users.
5. Optionally, select specific **CPU microarchitectures** (e.g., `zen3`, `skylake_avx512`)
   to further narrow the visible software builds.
6. If your offering has SLURM partitions defined, you can associate the catalog with a
   specific **partition**.

!!! tip
    Only system administrators can import and update software catalogs.
    Service providers can link existing catalogs to their offerings.

## How users see software packages

When a catalog is linked to an offering, a **Software** tab appears on the public
offering page. Users can:

- **Browse packages** in a searchable, filterable table.
- **Filter** by catalog type, category, license, GPU architecture, and toolchain.
- **Expand a package** to see:
    - Description and categories
    - Available versions with compatible hardware targets
    - GPU architecture badges for GPU-enabled builds
    - `module load` command for each version (copy to clipboard)
- **Identify extension packages** by the "Extension" badge next to the package name.
- **See parent packages** for extensions (shown as "Extends: PackageName (versions)").
- **View extension packages** listed under the parent package with their version numbers.

### Package types

Software packages can be either **standalone** or **extensions**:

- **Standalone packages** (e.g., GROMACS, TensorFlow) are self-contained software.
- **Extension packages** (e.g., GROMACS-PLUMED) extend a parent package with additional
  functionality. Extensions display an "Extension" badge and show which parent
  package they extend.

## Administration

### Importing catalogs

System administrators can import catalogs from the **Administration** > **Software catalog** page:

1. Click **Check for updates** to discover available upstream catalogs.
2. Select a catalog and click **Import** to load it into the system.
3. Imported catalogs can be updated by clicking **Update catalog** to sync with the
   upstream source.

### Catalog types

| Type | Description | Example |
|------|-------------|---------|
| Binary runtime | Pre-built software stacks | EESSI |
| Source package | Build-from-source packages | Spack |
| Package manager | Language-ecosystem package managers | conda, pip |

### Settings

Software catalog settings are organized into three groups accessible from the
administration page:

- **General** - Common settings for all catalog types
- **EESSI** - Settings specific to EESSI catalog integration
- **Spack** - Settings specific to Spack catalog integration
