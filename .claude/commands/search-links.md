# Search Link Database

Search and filter the link-dumps database.

## Usage

```
/search-links <query> [options]
```

## Query Types

1. **Text search** - Search titles, URLs, notes
   ```
   /search-links alignment faking
   ```

2. **Tag filter** - Filter by tags (prefix with #)
   ```
   /search-links #ai-safety #evaluations
   ```

3. **Importance filter** - Filter by importance level
   ```
   /search-links importance:high
   /search-links importance:very-high
   ```

4. **Source filter** - Filter by source
   ```
   /search-links source:arxiv
   /search-links source:anthropic
   ```

5. **Combined** - Combine multiple filters
   ```
   /search-links alignment #arxiv importance:high
   ```

## Output

Display matching links with:
- ID and title
- URL
- Tags
- Importance level
- Notes preview (if any)

## Examples

```
/search-links red teaming
/search-links #interpretability #paper
/search-links 2024 #ai-safety importance:high
```
